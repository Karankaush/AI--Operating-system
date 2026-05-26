import os
from typing import List
from urllib import response

from dotenv import load_dotenv
from langchain_core import messages
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from rag.vectorstore import load_vectorstore

from langgraph.types import Send

from state import State


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


model = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0.7,
)


search_tool = DuckDuckGoSearchRun()

vectorstore = load_vectorstore()


retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


class Task(BaseModel):

    task: str = Field(
        ...,
        description="Task description"
    )

    tool: str = Field(
    ...,
    description="""
    Tool required for this task.

    Available tools:
    - research
    - calculator
    - rag
    - llm
    """
    )



class PlannerOutput(BaseModel):

    tasks: List[Task]


structured_llm = model.with_structured_output(PlannerOutput)


# def rag_worker(state):

#     task = state["task"]


#     results = retriever.invoke(task)


#     context = "\n\n".join(
#         [doc.page_content for doc in results]
#     )


#     return {
#         "rag_results": [context],
#         "used_tools": ["rag"]
#     }


def rag_worker(state):

    print("\n===== RAG WORKER =====")

    task = state["task"]

    print("TASK:", task)

    results = retriever.invoke(task)

    print("RESULTS FOUND:", len(results))


    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    print("CONTEXT:", context[:500])

    return {
        "rag_results": [context],
        "used_tools": ["rag"]
    }

def calculator_worker(state):

    task = state["task"]

    prompt = f"""
    Solve this mathematical task:

    {task}

    Return only the answer.
    """

    response = model.invoke(prompt)

    return {
        "calculator_results": [response.content]
    }


def planner(state: State):

    messages = state["messages"]

    user_message = messages[-1].content
    prompt = f"""
    You are a task planning agent.

    Your job:
    - Break the user request into meaningful actionable tasks.
    - Only generate actual user tasks.
    - Do NOT include instructions or meta steps.

    Tool selection rules:

    1. Use "rag"
    when the user asks about:
    - uploaded PDFs
    - documents
    - files
    - notes
    - summaries of uploaded content
    - explanations from uploaded documents

    2. Use "research"
    for latest/current web information.

    3. Use "calculator"
    for math/calculations.

    4. Use "llm"
    for normal conversation/general reasoning.

    User Request:
    {user_message}
    """

    response = structured_llm.invoke(prompt)
    print("\n===== PLANNER OUTPUT =====")
    print(response)

    return {
        "tasks": [task.model_dump() for task in response.tasks]
    }


def assign_workers(state: State):

    sends = []

    for task in state["tasks"]:

        if task["tool"] == "research":

            sends.append(
                Send(
                    "research_worker",
                    {
                        "task": task["task"]
                    }
                )
            )


        elif task["tool"] == "calculator":

            sends.append(
                Send(
                    "calculator_worker",
                    {
                        "task": task["task"]
                    }
                )
            )


        elif task["tool"] == "rag":

            sends.append(
                Send(
                    "rag_worker",
                    {
                        "task": task["task"]
                    }
                )
            )


        elif task["tool"] == "llm":

            return "chatbot"


    if not sends:

        return "chatbot"


    return sends


# def assign_workers(state: State):

#     sends = []

#     for task in state["tasks"]:

#         if task["tool"] == "research":

#             sends.append(
#                 Send(
#                     "research_worker",
#                     {
#                         "task": task["task"]
#                     }
#                 )
#             )


#         elif task["tool"] == "calculator":

#             sends.append(
#                 Send(
#                     "calculator_worker",
#                     {
#                         "task": task["task"]
#                     }
#                 )
#             )


#         elif task["tool"] == "rag":

#             sends.append(
#                 Send(
#                     "rag_worker",
#                     {
#                         "task": task["task"]
#                     }
#                 )
#             )


#     return sends if sends else "chatbot"

def research_worker(state):

    task = state["task"]

    result = search_tool.invoke(task)

    return {
        "research_results": [result]
    }


def chatbot(state: State):
    messages = state["messages"]


    research_results = state.get(
        "research_results",
        []
    )

    calculator_results = state.get(
        "calculator_results",
        []
    )
    rag_results = state.get(
    "rag_results",
    []
    )
    system_message = SystemMessage(
        content=f"""
        You are an AI Operating System assistant.

    Rules:
    - Give concise responses.
    - Avoid unnecessary explanations.
    - Avoid repeating conversation history.
    - Answer directly.
    - Keep responses short unless user asks for detail.
    - Use RAG context only when relevant.

        Research Results:
        {research_results}

        Calculator Results:
        {calculator_results}

        RAG Results:
        {rag_results}
        """
    )

    print("\n===== CHATBOT =====")
    print("RAG RESULTS:", rag_results)

    response = model.invoke(
        [system_message] + messages
    )



    return {
        "messages": [response]
    }