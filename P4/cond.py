from typing import TypedDict

class CounterState(TypedDict):
    counter: int

class UserInputState(TypedDict):
    user_input: str

def get_user_input(state: CounterState) -> UserInputState:
    print(f"Counter value: {state['counter']}")
    user_input = input("Input (+, -, .): ")
    return {"user_input": user_input}

def increment(state: CounterState) -> CounterState:
    return {"counter": state["counter"] + 1}

def decrement(state: CounterState) -> CounterState:
    return {"counter": state["counter"] - 1}

from langgraph.graph import StateGraph, START, END
graph = StateGraph(CounterState)

graph.add_node("get_user_input", get_user_input)
graph.add_node("increment", increment)
graph.add_node("decrement", decrement)

graph.add_edge(START, "get_user_input")

def check_user_input(state: UserInputState):
    actions = { "+": "increment", "-": "decrement" }
    return actions.get(state["user_input"], "exit")

graph.add_conditional_edges("get_user_input",
        check_user_input,
        {"increment": "increment", "decrement": "decrement", "exit": END})

graph.add_edge("increment", "get_user_input")
graph.add_edge("decrement", "get_user_input")

app = graph.compile()

with open("cond.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())

response = app.invoke({"counter": 0})
print(response)
