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

SYSTEM_PROMPT = """
You are a Python programming tutor.

When answering a programming concept question:
1. Give a short explanation.
2. Give 3 important points.
3. Give an example.
4. Give Python code.

When a question requires calculation or verification,
use the appropriate MCP tool.

After receiving the tool result, explain the result
to the student in simple language.

Do not use tools when they are unnecessary.
""".strip()


def print_execution(result: dict) -> None:
    print("\n" + "=" * 60)
    print("              AGENT EXECUTION")
    print("=" * 60)

    for index, message in enumerate(result["messages"], start=1):
        print(f"\n--- MESSAGE {index} ---")
        print("TYPE:", message.type)

        if message.type == "human":
            print("USER:")
            print(message.content)

        elif message.type == "ai":
            tool_calls = getattr(message, "tool_calls", None)
            if tool_calls:
                print("\n>>> GEMINI SELECTED TOOL <<<")
                for tool_call in tool_calls:
                    print("TOOL:", tool_call["name"])
                    print("ARGUMENTS:", tool_call["args"])
            elif message.content:
                print("AI:")
                print(message.content)

        elif message.type == "tool":
            print("\n>>> MCP TOOL RESULT <<<")
            print("TOOL:", message.name)
            print("RESULT:", message.content)


async def main() -> None:
    tools = await client.get_tools()

    print("\n=== MCP TOOLS DISCOVERED ===")
    for tool in tools:
        print(f"- {tool.name}")

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )

    messages = []

    print("\nAI Tutor Agent ready. Type 'quit' to exit.\n")

    while True:
        question = input("You: ").strip()
        if not question:
            continue
        if question.lower() in {"quit", "exit", "q"}:
            break

        messages.append({"role": "user", "content": question})

        result = await agent.ainvoke({"messages": messages})
        print_execution(result)

        final_message = result["messages"][-1]
        print("\n" + "=" * 60)
        print("                 FINAL ANSWER")
        print("=" * 60)
        print(final_message.content)
        print()

        messages = result["messages"]


if __name__ == "__main__":
    asyncio.run(main())
