# server.py
from fastmcp import FastMCP
from fastmcp.server.proxy import ProxyClient

# Create a proxy to the logfire-mcp server
mcp = FastMCP.as_proxy(
    ProxyClient("uvx logfire-mcp@latest"),
    name="logfire-proxy"
)
