# AI Tutor Agent

Python programming tutor built with LangChain, Gemini, and MCP tools.

The agent answers coding questions. When a question needs a check
(palindrome, prime, Fibonacci, GCD, and similar), it calls tools from
`mcp_server.py` and then explains the result in plain language.

## Stack

- LangChain `create_agent`
- Gemini (`gemini-2.5-flash`)
- MCP server (`FastMCP`) over stdio
- LangGraph smoke test in `test_langgraph.py`

## Project layout

```
programming-tutor-agent/
  main.py              # single-turn chat
  tutor_agent.py       # multi-turn tutor with tool traces
  mcp_server.py        # MCP tools the agent can call
  test_langgraph.py    # small LangGraph check
  requirements.txt
  .env.example
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

Single question:

```bash
python main.py
```

Interactive tutor (type `quit` to stop):

```bash
python tutor_agent.py
```

LangGraph check:

```bash
python test_langgraph.py
```

Run the MCP server alone:

```bash
python mcp_server.py
```

## MCP Inspector (demo in the video)

```bash
npx @modelcontextprotocol/inspector python mcp_server.py
```

Open the Inspector, go to **Tools**, then execute `check_prime`, `reverse_string`, `sum_of_digits`, or `check_leap_year`.

## Same tools from Codex / Cursor

Use `mcp.json` in this folder so the client can call the programming-tutor server. Demo prompts:

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
