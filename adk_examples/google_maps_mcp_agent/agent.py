import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, \
                StdioServerParameters, StdioConnectionParams
from dotenv import load_dotenv

# Task 2. Using Google Maps MCP server with ADK agents (ADK as an MCP client) in adk web
# This section demonstrates how to integrate tools from an external Google Maps MCP server into your ADK agents. 
# This is the most common integration pattern when your ADK agent needs to use capabilities provided by an existing service that exposes an MCP interface. 
# You will see how the MCPToolset class can be directly added to your agent's tools list, enabling seamless connection to an MCP server, 
# discovery of its tools, and making them available for your agent to use. 

load_dotenv()
google_maps_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")

if not google_maps_api_key:
    print("WARNING: GOOGLE_MAPS_API_KEY is not set. Please set it as an environment variable or update it in the script.")

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='maps_assistant_agent',
    instruction='Help the user with mapping, directions, and finding places using Google Maps tools.',

    ## Add the MCPToolset below:
    tools=[
        MCPToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command='npx',
                args=[
                    "-y",
                    "@modelcontextprotocol/server-google-maps",
                ],
                env={
                    "GOOGLE_MAPS_API_KEY": google_maps_api_key
                }
            ),
            timeout=15,
            ),
        )
    ],
)



