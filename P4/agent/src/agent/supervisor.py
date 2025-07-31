from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b
add_agent = create_react_agent(llm, [add],
    prompt="You are a math assistant. You can use tools to perform addition.",
    name="add assistant"
)

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b
multiply_agent = create_react_agent(llm, [multiply],
    prompt="You are a math assistant. You can use tools to perform multiplication.",
    name="multiply assistant"
)

from langgraph_supervisor import create_supervisor
supervisor = create_supervisor([add_agent, multiply_agent],
    model=llm,
    prompt="You manage a math assistant. Assign work to them."
).compile()     # create_supervisor returns StateGraph

if __name__ == "__main__":
    from langchain_core.messages import HumanMessage

    response = supervisor.invoke({"messages": [HumanMessage(content="3에 2를 곱한 결과에 5를 더하면?")]})
    print(response)
    for m in response["messages"]:
        m.pretty_print()

    with open("supervisor.png", "wb") as f:
        f.write(supervisor.get_graph().draw_mermaid_png())