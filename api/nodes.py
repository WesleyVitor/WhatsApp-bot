
import os

from langgraph.graph.message import add_messages
from typing import TypedDict, Annotated
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
from twilio.rest import Client

class GraphState(TypedDict):
    messages: Annotated[list, add_messages]
    user_number: str

# Funções do grafo LangGraph
async def process_message(state: GraphState) -> GraphState:
    """
    Process message node
    """
    last_message = state.get("messages")[-1].content
    
    instructions = """
        You are a concise assistant
    """
    tavily_api_key = os.environ.get("TAVILY_API_KEY")
    params = {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavily_api_key}"
      ]
    }
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as tavily_server:
        agent = Agent(
            name="chatbot",
            instructions=instructions,
            model="gpt-4.1-mini",
            mcp_servers=[tavily_server]
        )

        with trace("investigate"):
            result = await Runner.run(agent, last_message)
            new_state = {
                "messages": [{"role": "system", "content": result.final_output}]
            }

    return new_state


def send_whatsapp_message(state: GraphState) -> GraphState:
    """
    SendWhatsappMessage node that send the final message from LLM to whatsapp

    """
    receive_number = state.get("user_number")
    last_message = state.get("messages")[-1].content

    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    from_number = os.environ.get("FROM_NUMBER")
    client = Client(account_sid, auth_token)

    client.messages.create(
        from_=f'whatsapp:{from_number}',
        body=last_message,
        to=receive_number
    )
    return state
