from typing import TypedDict, List

class State(TypedDict):
    user_message: str
    tasks: List[str]
    research_data: str
    require_research: bool
    response: str