import os
import asyncio

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


load_dotenv()

print("GOOGLE_API_KEY found:", bool(os.getenv("GOOGLE_API_KEY")))

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

client = MultiServerMCPClient(
    {
        "programming_tutor": {
            "transport": "stdio",
            "command": "python",
            "args": ["mcp_server.py"],
        }
    }
)


async def main() -> None:
    tools = await client.get_tools()

    print("\n=== MCP Tools ===")
    for tool in tools:
        print("-", tool.name)

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=(
            "You are a helpful Python programming tutor. "
            "Explain concepts clearly and briefly. "
            "Use MCP tools when they are useful. "
            "After using a tool, explain the result "
            "in simple language."
        ),
    )

    question = input("\nYou: ")

    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )

    response = result["messages"][-1].content
    print("\n=== AI ===")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
