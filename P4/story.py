from typing import TypedDict
class State(TypedDict):
    subject: str
    story: str
    criticism: str

def generate_story(state: State) -> State:
    """Generate a revised story based on the provided state."""
    if "story" not in state or state["story"] == "":
        return {"story": f"Story about {state['subject']} is generated."}
    return {"story": f"{state['story']} is revised based on the criticism: {state['criticism']}."}

def user_critic(state: State) -> State:
    criticism = input(f"Please provide your criticism on the story: {state['story']}\nCriticism: ")
    return {"criticism": criticism}

from langgraph.graph import StateGraph, START, END
graph = StateGraph(State)

graph.add_node("generate_story", generate_story)
graph.add_node("user_critic", user_critic)

graph.add_edge(START, "generate_story")
graph.add_edge("generate_story", "user_critic")

def check_user_criticism(state: State):
    if state["criticism"] != "": return "revise"
    return "exit"

graph.add_conditional_edges("user_critic",
        check_user_criticism,
        {"revise": "generate_story", "exit": END})

app = graph.compile()
response = app.invoke({"subject": "cat"})
print(response)
