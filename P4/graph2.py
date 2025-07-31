from typing import TypedDict

class InputState(TypedDict):
    input: str

class OutputState(TypedDict):
    output: str

class PrivateState(TypedDict):
    private: str

class OverallState(TypedDict):
    input: str
    output: str
    private: str

def node_1(state: InputState) -> PrivateState:
    return {"private": state["input"] + " love"}

def node_2(state: PrivateState) -> OutputState:
    return {"output": state["private"] + " AI."}

from langgraph.graph import StateGraph, START, END
graph = StateGraph(OverallState,
                   input_schema=InputState,
                   output_schema=OutputState)

graph.add_node("node_1", node_1)
graph.add_node("node_2", node_2)

graph.add_edge(START, "node_1")
graph.add_edge("node_1", "node_2")
graph.add_edge("node_2", END)

app = graph.compile()
response = app.invoke({"input": "I"})
print(response)  # {'output': 'I love AI.'}

with open("graph2.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())
