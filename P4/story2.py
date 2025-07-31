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

from langgraph.types import interrupt, Command
def user_critic(_: State) -> State:
    criticism = interrupt({"command": "critic story"})
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

from langgraph.checkpoint.memory import MemorySaver
app = graph.compile(checkpointer=MemorySaver())

config = {"configurable": {"thread_id": "1"}}
response = app.invoke({"subject": "cat"}, config=config)

while "__interrupt__" in response:
    for i in response["__interrupt__"]:
        if i.value["command"] == "critic story":
            criticism = input(f"Please provide your criticism on the story: {response['story']}\nCriticism: ")
            response = app.invoke(Command(resume=criticism), config=config)

print(response)