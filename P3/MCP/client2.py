from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_mcp_adapters.client import MultiServerMCPClient
client = MultiServerMCPClient(
    {
        "math": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",     # not "stramble-http" as in server2.py
        }
    }
)

import asyncio

async def main():
    tools = await client.get_tools()    # asynchronous call to get tools
    # StructuredTool does not support sync invocation.
    
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    prompt = ChatPromptTemplate.from_messages([
        ("system", "당신은 수학 문제를 푸는 도우미입니다. 도구를 사용해서 문제를 해결하세요."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    from langchain.agents import create_tool_calling_agent, AgentExecutor
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)

    response = await agent_executor.ainvoke({"input": "2와 3을 더한 결과에 5를 곱하면 얼마인가요?"})
    print(response)

if __name__ == "__main__":
    asyncio.run(main())