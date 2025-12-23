# server.py
import os

from dotenv import load_dotenv
from fastmcp import FastMCP
from fastmcp.client.transports import UvxStdioTransport

# Load environment variables from .env
load_dotenv()

# Create a proxy to the logfire-mcp server
mcp = FastMCP.as_proxy(
    UvxStdioTransport(
        tool_name="logfire-mcp",
        env_vars={"LOGFIRE_READ_TOKEN": os.environ["LOGFIRE_READ_TOKEN"]},
    ),
    name="logfire-proxy"
)
