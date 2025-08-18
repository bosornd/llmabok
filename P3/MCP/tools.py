from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_mcp_adapters.client import MultiServerMCPClient
client = MultiServerMCPClient(
    {
        "filesystem": {
            "command": "npx",
            "args": ["@modelcontextprotocol/server-filesystem", "./"],
            "transport": "stdio",
        },
        "wikipedia": {
            "command": "wikipedia-mcp",
            "args": ["--transport", "stdio"],
            "transport": "stdio",
        }
    }
)

import asyncio

async def main():
    tools = await client.get_tools()    # asynchronous call to get tools

    for tool in tools:
        print(f"Tool name: {tool.name}, Tool description: {tool.description}")

if __name__ == "__main__":
    asyncio.run(main())