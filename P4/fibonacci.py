import operator
from typing import TypedDict, Annotated, Literal

class FibonacciState(TypedDict):
    N: int
    fibonacci: Annotated[list[int], operator.add]
    result: int

def fibonacci(state: FibonacciState) -> FibonacciState:
    return {"fibonacci": [0, 1]} if len(state["fibonacci"]) == 0 else state

def calc_fibonacci(state: FibonacciState) -> FibonacciState:
    return {"fibonacci": [state["fibonacci"][-1] + state["fibonacci"][-2]] }

def exit_fibonacci(state: FibonacciState) -> FibonacciState:
    return {"result": state["fibonacci"][state["N"]] }

from langgraph.graph import StateGraph, START, END
graph = StateGraph(FibonacciState)

graph.add_node("fibonacci", fibonacci)
graph.add_node("calc_fibonacci", calc_fibonacci)
graph.add_node("exit_fibonacci", exit_fibonacci)

graph.add_edge(START, "fibonacci")

def check_fibonacci(state: FibonacciState) -> Literal["next", "exit"]:
    if len(state["fibonacci"]) <= state["N"]:
        return "next"
    return "exit"

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

with open("4-fibonacci.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())



from langgraph.checkpoint.memory import MemorySaver
app = graph.compile(checkpointer=MemorySaver())

config = {"configurable": {"thread_id": "1"}}
response = app.invoke({"N": 5, "fibonacci": [0, 1, 1, 2, 3]}, config=config)
print(response)
# {'N': 5, 'fibonacci': [0, 1, 1, 2, 3, 0, 1, 1, 2, 3], 'result': 0}

history = app.get_state_history(config=config)
for i, state in enumerate(history):
    print(f"Checkpoint {i}: {state}")
# [] --> START --> [0, 1, 1, 2, 3] --> fibonacci --> [0, 1, 1, 2, 3, 0, 1, 1, 2, 3]
# fibonacci node에서 state를 반환하면서 이전 fibonacci sequence가 중복됨