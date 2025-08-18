import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from typing import TypedDict
class State(TypedDict):
    subject: str
    story: str
    criticism: str

def generate_story(state: State) -> State:
    if "criticism" in state:
        prompt = f"다음 이야기와 비평에 대한 개선된 이야기를 작성해 주세요.\n"
        prompt += f"- 이야기: {state['story']}\n"
        prompt += f"- 비판: {state['criticism']}\n"
    else:
        prompt = f"다음 주제로 이야기를 작성해 주세요.\n- 주제: {state['subject']}\n"
    
    prompt += "이야기는 1000자 이내로 작성해 주시고, 이야기만 출력해 주세요."

    response = llm.invoke(prompt)
    state['story'] = response.content

    return state

from langgraph.types import interrupt
def user_critic(state: State) -> State:
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
response = app.invoke({"subject": "개와 고양이"}, config=config)

from langgraph.types import Command
while "__interrupt__" in response:
    for i in response["__interrupt__"]:
        if i.value["command"] == "critic story":
            state = app.get_state(config=config)
            print(f"이야기: {state.values['story']}")
            criticism = input("개선 사항을 입력하세요: ")
            response = app.invoke(Command(resume=criticism), config=config)

print(response)
