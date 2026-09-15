# AI Tutor Agent

Python programming tutor built with LangChain, Gemini, and MCP tools.

The agent answers coding questions. When a question needs a check
(palindrome, prime, Fibonacci, GCD, and similar), it calls tools from
`mcp_server.py` and then explains the result in plain language.

## Demo

Full walkthrough (VS Code + MCP Inspector + Codex calling the same 13 tools):

[Watch demo video](docs/demo.mp4)

![VS Code tutor project](docs/screenshots/01-vscode-tutor.png)

![MCP Inspector tool list](docs/screenshots/02-mcp-inspector-tools.png)

![check_prime in MCP Inspector](docs/screenshots/03-check-prime.png)

![reverse_string in MCP Inspector](docs/screenshots/04-reverse-string.png)

![Codex lists the 13 MCP tools](docs/screenshots/05-codex-list-tools.png)

![Codex check_leap_year 2005](docs/screenshots/06-leap-year.png)

What the demo shows:

1. Project files in VS Code (`tutor_agent.py`, `mcp_server.py`)
2. MCP Inspector connected to `Programming Tutor`
3. Live tool runs: `check_prime(6)`, `reverse_string("hello")`, `sum_of_digits`
4. Codex discovering all 13 tools and running `check_leap_year(2005)` → not a leap year

## Stack

- LangChain `create_agent`
- Gemini (`gemini-2.5-flash`)
- MCP server (`FastMCP`) over stdio
- LangGraph smoke test in `test_langgraph.py`

## Project layout

```
programming-tutor-agent/
  main.py
  tutor_agent.py
  mcp_server.py
  test_langgraph.py
  requirements.txt
  .env.example
  mcp.json
  docs/demo.mp4
  docs/screenshots/
```

## Setup

```bash
cd programming-tutor-agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Put your Gemini key in `.env`:

```
GOOGLE_API_KEY=your_key
```

## Run

```bash
python main.py
python tutor_agent.py
python test_langgraph.py
python mcp_server.py
```

## MCP Inspector

```bash
npx @modelcontextprotocol/inspector python mcp_server.py
```

## Same tools from Codex / Cursor

Use `mcp.json` so the client can call the programming-tutor server.

- List the tools available from the programming-tutor MCP server
- `check_leap_year` for `2005` → not a leap year

## MCP tools

- `check_palindrome`
- `check_armstrong`
- `fibonacci`
- `check_prime`
- `factorial`
- `reverse_string`
- `check_even_odd`
- `sum_of_digits`
- `gcd`
- `lcm`
- `check_leap_year`
- `count_vowels`
- `check_anagram`

## Example prompts

- Is 153 an Armstrong number?
- Check if "A man a plan a canal Panama" is a palindrome
- What is Fibonacci(10)?
- Explain list comprehensions in Python
- Are listen and silent anagrams?
