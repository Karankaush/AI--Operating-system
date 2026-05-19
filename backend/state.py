from typing import TypedDict, List
from typing_extensions import Annotated

from operator import add


class State(TypedDict):

    messages: Annotated[List, add]

    tasks: List[dict]

    research_results: Annotated[List[str], add]

    calculator_results: Annotated[List[str], add]

    response: str