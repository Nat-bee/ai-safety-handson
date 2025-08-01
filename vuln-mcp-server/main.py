# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "mcp",
# ]
# ///

from mcp.server.fastmcp import FastMCP
import time
import os
import platform

mcp = FastMCP("Super MCP Server", "1.0.0")


@mcp.tool()
def current_time() -> int:
    """Get the current time in seconds since the epoch."""
    return int(time.time())

@mcp.resource("info://{name}")
def get_info(name: str) -> str:
    """Get a information."""
    if name in (os.getenv("USER"), os.getenv("USERNAME")):
        flag = "flag{hello_mcp_server}"
        return f"User info: {name}, {platform.system()} {platform.release()} - {flag}"

    return f"OS info {platform.system()} {platform.release()}"

if __name__ == "__main__":
    mcp.run()
