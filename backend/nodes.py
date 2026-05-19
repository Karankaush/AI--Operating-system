import os
from typing import List

from dotenv import load_dotenv

from pydantic import BaseModel, Field

from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

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
        - llm
        """
    )




class PlannerOutput(BaseModel):

    tasks: List[Task]


structured_llm = model.with_structured_output(PlannerOutput)


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

    user_message = state["user_message"]

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

    research_results = state.get(
        "research_results",
        []
    )

    calculator_results = state.get(
        "calculator_results",
        []
    )

    prompt = f"""
    Generate a final response using:

    Research Results:
    {research_results}

    Calculator Results:
    {calculator_results}
    """

    response = model.invoke(prompt)

    return {
        "response": response.content
    }