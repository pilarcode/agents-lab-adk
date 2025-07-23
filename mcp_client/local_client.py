import asyncio
from fastmcp import Client, FastMCP


# Local client
client = Client("D:\ia_projects\mcp_proyecto\mcp_platform\mcp_catalogue\mcp_servers\hello\server.py")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        print(f"TOOLS: {tools}\n")
        
        resources = await client.list_resources()
        print(f"RESOURCES: {resources}\n")

        prompts = await client.list_prompts()
        print(f"PROMPTS: {prompts}\n")
        
        # Execute operations
        print("Calling  an mcp tool: Adding 1 + 1")
        result = await client.call_tool("add", {"a": 1, "b": 1})
        print(result)

asyncio.run(main())