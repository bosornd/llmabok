import operator
from typing import TypedDict, Annotated, Literal
class FibonacciState(TypedDict):
    N: int
    fibonacci: Annotated[list[int], operator.add]
    result: int

def check_fibonacci(state: FibonacciState) -> Literal["next", "exit"]:
    if len(state["fibonacci"]) <= state["N"]:
        return "next"
    return "exit"

def fibonacci(state: FibonacciState) -> FibonacciState:
    return {"fibonacci": [0, 1]} if len(state["fibonacci"]) == 0 else state

def calc_fibonacci(state: FibonacciState) -> FibonacciState:
    n = len(state["fibonacci"])
    next_value = state["fibonacci"][n - 1] + state["fibonacci"][n - 2]
    return {"fibonacci": [next_value] }

def exit_fibonacci(state: FibonacciState) -> FibonacciState:
    return {"result": state["fibonacci"][state["N"]] }

from langgraph.graph import StateGraph, START, END
graph = StateGraph(FibonacciState)

graph.add_node("fibonacci", fibonacci)
graph.add_node("calc_fibonacci", calc_fibonacci)
graph.add_node("exit_fibonacci", exit_fibonacci)

graph.add_edge(START, "fibonacci")
graph.add_conditional_edges("fibonacci", check_fibonacci, {
    "next": "calc_fibonacci",
    "exit": "exit_fibonacci"
})
graph.add_conditional_edges("calc_fibonacci", check_fibonacci, {
    "next": "calc_fibonacci",
    "exit": "exit_fibonacci"
})
graph.add_edge("exit_fibonacci", END)
app = graph.compile()
response = app.invoke({"N": 10})
print(response)
# {'N': 10, 'fibonacci': [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], 'result': 55}

response = app.invoke({"N": 5, "fibonacci": [0, 1, 1, 2, 3]})
print(response)
"""
이미 계산된 피보나치 수열을 재사용하는 예시.
이 경우, START 노드에서 fibonacci 노드로 이동하면서 상태가 다음과 같이 변경됨.
{"fibonacci": [0, 1, 1, 2, 3, 0, 1, 1, 2, 3]}
<-- START 노드는 입력 상태가 그대로 유지되어야 하므로... DEFECT이라고 할 수 있음.
"""