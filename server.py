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
    # Local STDIO transport (for ChatGPT Desktop)
    mcp.run()
