🧠 The Fastest AI Travel Agent with SambaNova + PraisonAI Agents + Airbnb MCP
This project shows how to build a blazing-fast AI agent that searches for apartments on Airbnb using the SambaNova Meta-Llama-3.1 8B Instruct model, integrated via the PraisonAI Agents framework, and powered by MCP (Multi-Channel Protocol) for tool execution.

🏠 Say: "Find me an apartment in Paris from April 28 to April 30 for 2 adults"
⚡ And this AI agent finds the best options instantly.

🚀 Features
🧠 Uses SambaNova LLM via litellm

🔌 Connects to Airbnb through MCP (@openbnb/mcp-server-airbnb)

🗣️ Accepts simple natural language input

⚡ Returns results fast with zero setup on frontend

🛠️ Lightweight and developer-friendly

📦 Requirements
Python 3.10 or higher

Node.js installed

SambaNova API key (free or paid)

🛠️ Installation
pip install "praisonaiagents[llm]"
🔐 Setup
import os
os.environ["SAMBANOVA_API_KEY"] = "your_sambanova_api_key"

🎯 Result
💬 The agent uses Airbnb's API to return a list of apartments that match the input query, powered by real-time tool execution and fast LLM inference.
