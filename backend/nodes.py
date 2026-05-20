import os
from typing import List

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


def rag_worker(state):
    task = state["task"]
    result = retriever.invoke(task)

    context = "\n".join([doc.page_content for doc in result])
    return {
        "research_results": [context]
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

    prompt = f""" You are a task planning agent.

    Your job:
    - Break the user request into meaningful actionable tasks.
    - Only generate actual user tasks.
    - Do NOT include instructions or meta steps.
    - For each task determine whether web research is needed.

    User Request:
    {user_message}
    """

    response = structured_llm.invoke(prompt)

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

    if not sends:
        return "chatbot"

    return sends


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
        You are a helpful AI assistant.

        Use memory naturally.

        Research Results:
        {research_results}

        Calculator Results:
        {calculator_results}

        RAG Results:
        {rag_results}
        """
    )

    response = model.invoke(
        [system_message] + messages
    )



    return {
        "messages": [response]
    }