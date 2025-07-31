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

from langgraph.prebuilt import create_react_agent
agent = create_react_agent(llm, tools=[add, multiply])

from langchain_core.messages import HumanMessage
response = agent.invoke({"messages": [HumanMessage(content="2에 3을 더한 결과에 5를 곱하면?")]})

for m in response["messages"]:
    m.pretty_print()
