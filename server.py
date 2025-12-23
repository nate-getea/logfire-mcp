# server.py
from fastmcp import FastMCP
from fastmcp.client.transports import UvxStdioTransport

# Create a proxy to the logfire-mcp server
mcp = FastMCP.as_proxy(
    UvxStdioTransport(tool_name="logfire-mcp"),
    name="logfire-proxy"
)
