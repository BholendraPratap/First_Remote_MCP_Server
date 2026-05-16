#this file is extra file and this is only for intial stage for creating demo server and whole repo is of trial expense server.
import random 
from fastmcp import FastMCP

mcp = FastMCP("Demo")


@mcp.tool
def  roll_dice(n_dice: int=1) -> list[int]:
    """Roll n-dice  6 sided dice and return the results"""
    return [random.randint(1, 6) for _ in range(n_dice)]



@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()