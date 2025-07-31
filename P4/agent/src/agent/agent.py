from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b

tools = [add, multiply]

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.messages import SystemMessage
system_message = SystemMessage(
    content="You are a math assistant. You can use tools to perform calculations."
)

from pydantic import BaseModel, Field
class Answer(BaseModel):
    """Answer to the question."""
    number: int = Field(description="the calculated result")

from langgraph.prebuilt import create_react_agent
math_agent = create_react_agent(llm, tools=[add, multiply],
                                prompt=system_message,
                                response_format=Answer
                               )

if __name__ == "__main__":
    from langchain_core.messages import HumanMessage
    response = math_agent.invoke({"messages": [HumanMessage(content="2에 3을 더한 결과에 5를 곱하면?")]})

    for m in response["messages"]:
        m.pretty_print()

    print("Answer:", response["structured_response"].number)

    with open("agent.png", "wb") as f:
        f.write(math_agent.get_graph().draw_mermaid_png())