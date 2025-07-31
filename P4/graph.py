from typing import TypedDict
class CounterState(TypedDict):
    counter: int

from langgraph.graph import StateGraph, START, END
graph = StateGraph(CounterState)

def increment(state: CounterState) -> CounterState:
    state["counter"] += 1
    return state

graph.add_node("increment", increment)

graph.add_edge(START, "increment")
# graph.set_entry_point("increment")

graph.add_edge("increment", END)
# graph.set_finish_point("increment")

app = graph.compile()
response = app.invoke({"counter": 0})
print(response)  # {'counter': 1}

with open("graph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())
