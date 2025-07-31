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
    # StructuredTool does not support sync invocation.

    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    prompt = ChatPromptTemplate.from_messages([
        ("system", "당신은 도구를 사용하는 AI입니다."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    from langchain.agents import create_tool_calling_agent, AgentExecutor
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)

    response = agent_executor.invoke({"input": "2와 3을 더하면 얼마인가요?"})
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
