import operator
from typing import TypedDict, Annotated, Literal

class FibonacciState(TypedDict):
    N: int
    fibonacci: Annotated[list[int], operator.add]
    result: int
