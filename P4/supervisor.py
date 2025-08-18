import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b

from langgraph.prebuilt import create_react_agent
adder_agent = create_react_agent(llm, tools=[add], name="adder")
multiplier_agent = create_react_agent(llm, tools=[multiply], name="multiplier")

from langgraph_supervisor import create_supervisor
app = create_supervisor([adder_agent, multiplier_agent],
    model=llm, prompt="You manage math assistants. Assign work to them."
).compile()     # create_supervisor returns StateGraph

with open("supervisor.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())

from langchain_core.messages import HumanMessage
response = app.invoke({"messages": [HumanMessage("2에 3을 더한 결과에 5를 곱하면?")]})

for m in response["messages"]:
    m.pretty_print()

with open("supervisor.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())