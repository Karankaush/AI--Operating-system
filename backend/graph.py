from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from state import State

from nodes import (
    calculator_worker,
    planner,
    chatbot,
    research_worker,
    assign_workers
)


graph = StateGraph(State)


graph.add_node("planner", planner)

graph.add_node("research_worker", research_worker)

graph.add_node("calculator_worker",calculator_worker)

graph.add_node("chatbot", chatbot)


graph.add_edge(START, "planner")


graph.add_conditional_edges(
    "planner",
    assign_workers,
    {
        "research_worker": "research_worker",
        "calculator_worker": "calculator_worker",
        "chatbot": "chatbot"
    }
)
graph.add_edge(
    "calculator_worker",
    "chatbot"
)


graph.add_edge("research_worker", "chatbot")

graph.add_edge("chatbot", END)

memory = MemorySaver()
workflow = graph.compile(
    checkpointer=memory
)