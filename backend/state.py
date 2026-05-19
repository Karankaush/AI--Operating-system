from typing import TypedDict, List
from typing_extensions import Annotated

from operator import add


class State(TypedDict):

    user_message: str

    tasks: List[dict]

    research_results: Annotated[List[str], add]

    calculator_results: Annotated[List[str], add]

    response: str