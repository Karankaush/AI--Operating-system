from langgraph.graph import StateGraph, START, END

from state import State
from nodes import chatbot, planner, researcher

graph = StateGraph(State)
graph.add_node("planner", planner)
graph.add_node("researcher", researcher)
graph.add_node("chatbot", chatbot)
graph.add_edge(START, "planner")
graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "chatbot")
graph.add_edge("chatbot", END)

graph_test = graph.compile()
