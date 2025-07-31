import operator
from typing import TypedDict, Annotated, Literal
class FibonacciState(TypedDict):
    N: int
    fibonacci: list[int]
    result: int

def check_fibonacci(state: FibonacciState) -> Literal["next", "exit"]:
    if len(state["fibonacci"]) <= state["N"]:
        return "next"
    return "exit"

def fibonacci(state: FibonacciState) -> FibonacciState:
    return {"fibonacci": [0, 1]} if "fibonacci" not in state or len(state["fibonacci"]) < 2 else state

def calc_fibonacci(state: FibonacciState) -> FibonacciState:
    state["fibonacci"].append(state["fibonacci"][-1] + state["fibonacci"][-2])
    return state

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

from langgraph.checkpoint.memory import MemorySaver
app = graph.compile(checkpointer=MemorySaver())

config = {"configurable": {"thread_id": "user_1"}}

while True:
    N = int(input("N 값을 입력하세요 (종료하려면 음수 입력): "))
    if N < 0: break

    state = app.get_state(config=config)
    state.values["N"] = N
    response = app.invoke(state.values, config=config)
    print(response)
    print(f"Fibonacci({N}) = {response['result']}")
