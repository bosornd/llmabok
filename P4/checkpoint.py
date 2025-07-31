#################################### sub-graph #####################################
from typing import TypedDict
class CounterState(TypedDict):
    counter: int

def increment(state: CounterState):
    return {"counter": state["counter"] + 1}

def decrement(state: CounterState):
    return {"counter": state["counter"] - 1}

from langgraph.graph import StateGraph, START, END

def create_simple_graph(name: str, func: callable):     # -> CompiledStateGraph
    graph = StateGraph(CounterState)
    graph.add_node(name, func)
    graph.set_entry_point(name)
    graph.set_finish_point(name)

    return graph.compile()

inc_graph = create_simple_graph("increment", 
                                lambda state: {"counter": state["counter"] + 1})

dec_graph = create_simple_graph("decrement", 
                                lambda state: {"counter": state["counter"] - 1})

#################################### main-graph ####################################

class UserInputState(TypedDict):
    user_input: str

def get_user_input(state: CounterState) -> UserInputState:
    print(f"Counter value: {state['counter']}")
    user_input = input("Input (+, -, .): ")
    return {"user_input": user_input}

graph = StateGraph(CounterState)
graph.add_node("get_user_input", get_user_input)
graph.add_node("increment", inc_graph)
graph.add_node("decrement", dec_graph)

graph.add_edge(START, "get_user_input")
graph.add_conditional_edges("get_user_input",
        lambda state: "increment" if state["user_input"] == "+" else "decrement" if state["user_input"] == "-" else "exit",
        {"increment": "increment", "decrement": "decrement", "exit": END})
graph.add_edge("increment", "get_user_input")
graph.add_edge("decrement", "get_user_input")

from langgraph.checkpoint.memory import MemorySaver
app = graph.compile(checkpointer=MemorySaver())

config = {"configurable": {"thread_id": "user_1"}}

response = app.invoke({"counter": 0}, config=config)
history = app.get_state_history(config=config)
for i, state in enumerate(history):
    print(f"Checkpoint {i}: {state}")
print(response)

state = app.get_state(config=config)
response = app.invoke(state.values, config=config)
print(response)
