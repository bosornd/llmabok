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

tools = [add, multiply]
tools_by_name = {tool.name: tool for tool in tools}

llm_with_tools = llm.bind_tools(tools)

from langgraph.graph import MessagesState

def llm_call(state: MessagesState):
    """LLM decides whether to call a tool or not"""
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

from langchain_core.messages import ToolMessage
def tool_node(state: MessagesState):
    """Performs the tool call"""

    messages = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        response = tool.invoke(tool_call["args"])
        messages.append(ToolMessage(content=response,
                                    tool_call_id=tool_call["id"]))

    return {"messages": messages}

def should_continue(state: MessagesState):
    """Decide if we should continue the loop or stop
       based upon whether the LLM made a tool call"""

    if state["messages"][-1].tool_calls: return "tool"
    return "exit"

from langgraph.graph import StateGraph, START, END
graph = StateGraph(MessagesState)

graph.add_node("llm_call", llm_call)
graph.add_node("tool_node", tool_node)

graph.add_edge(START, "llm_call")
graph.add_edge("tool_node", "llm_call")

graph.add_conditional_edges(
    "llm_call",
    should_continue,
    {"tool": "tool_node", "exit": END},
)

from langchain_core.messages import HumanMessage
app = graph.compile()
response = app.invoke({"messages": [HumanMessage(content="1 + 2 * 3?")]})
print(response)

for m in response["messages"]:
    m.pretty_print()

with open("tool-node.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())