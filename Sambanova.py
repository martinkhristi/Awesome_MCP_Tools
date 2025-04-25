import os
import litellm
litellm._turn_on_debug()

# Set your SambaNova API Key
os.environ["SAMBANOVA_API_KEY"] = "SAMBANOVA_API_KEY"

from praisonaiagents import Agent, MCP

# Create the agent using SambaNova LLM
search_agent = Agent(
 instructions="You help book apartments on Airbnb.",
 llm="sambanova/Meta-Llama-3.1-8B-Instruct", # ✅ Official SambaNova model
 tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
)

# Start the Airbnb booking search
search_agent.start(
 "MUST USE airbnb_search Tool to Search. Search for Apartments in Paris for 2 nights. 04/28 - 04/30 for 2 adults. All Your Preference"
)