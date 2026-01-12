
import os

def view_mcp():
    """Parses and displays an MCP file."""
    mcp_file = "output.mcp"
    if not os.path.exists(mcp_file):
        print(f"Error: MCP file '{mcp_file}' not found.")
        print("Please run the MCP generator first.")
        return

    with open(mcp_file, "r") as f:
        lines = f.readlines()

    print("--- MCP Data ---")
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            print(f"{key.strip()}: {value.strip()}")
    print("----------------")

if __name__ == "__main__":
    view_mcp()
