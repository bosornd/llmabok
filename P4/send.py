from typing import TypedDict, Annotated
import operator
class State(TypedDict):
    input: list[list[int]] | list[int]
    intermediate: Annotated[list[int], operator.add]
    output: int

def find_max(state: State) -> State:
    return {"intermediate": [max(state["input"])]}

def collect_max(state: State) -> State:
    return {"output": max(state["intermediate"])}

from langgraph.types import Send
def distribute_max(state: State) -> list[Send]:
    return [Send("find_max", {"input": numbers}) for numbers in state["input"]]

from langgraph.graph import StateGraph, START, END
graph = StateGraph(State)

graph.add_node("find_max", find_max)
graph.add_node("collect_max", collect_max)

graph.add_conditional_edges(START, distribute_max, ["find_max"])
graph.add_edge("find_max", "collect_max")
graph.add_edge("collect_max", END)
app = graph.compile()
response = app.invoke({"input": [[4, 6, 5], [9, 2, 3], [7, 1, 8]]})
print(response)
# {'input': [[4, 6, 5], [9, 2, 3], [7, 1, 8]], 'intermediate': [6, 9, 8], 'output': 9}