from dotenv import load_dotenv
load_dotenv()

from langchain_mcp_adapters.client import MultiServerMCPClient
client = MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            "args": ["server.py"],
            "transport": "stdio",
        }
    }
)

import asyncio

async def main():
    tools = await client.get_tools()    # asynchronous call to get tools

    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    # pip install langgraph
    from langgraph.prebuilt import create_react_agent
    agent = create_react_agent(llm, tools)

    response = await agent.ainvoke({"messages": "2와 3을 더하면 얼마인가요?"})
#    print(response)

    for message in response["messages"]:
        message.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())
