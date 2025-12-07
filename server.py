from fastmcp import FastMCP

mcp = FastMCP("math-mcp-server")

@mcp.tool()
def add(a: float, b: float) -> float:
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    return a * b

if __name__ == "__main__":
    mcp.run(
        transport="websocket",
        host="0.0.0.0",   # Allow external devices
        port=5000         # Any port you want
    )
