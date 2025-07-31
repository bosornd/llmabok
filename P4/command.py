from typing import TypedDict

class CounterState(TypedDict):
    counter: int

from langgraph.types import Command
def get_user_input(state: CounterState) -> Command:
    print(f"Counter value: {state['counter']}")
    user_input = input("Input (+, -, .): ")
    actions = { "+": Command(goto="increment"), "-": Command(goto="decrement") }
    return actions.get(user_input, None)   # Command(goto=END)

def increment(state: CounterState):
    return Command(update={"counter": state["counter"] + 1}, goto="get_user_input")

def decrement(state: CounterState):
    return Command(update={"counter": state["counter"] - 1}, goto="get_user_input")

from langgraph.graph import StateGraph
graph = StateGraph(CounterState)

graph.add_node("get_user_input", get_user_input)
graph.add_node("increment", increment)
graph.add_node("decrement", decrement)

graph.set_entry_point("get_user_input")
app = graph.compile()

with open("command.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())

response = app.invoke({"counter": 0})
print(response)
