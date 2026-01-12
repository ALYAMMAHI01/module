
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

    mcp_data = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            mcp_data[key.strip()] = value.strip()

    print("--- MCP Data ---")
    print(f"Date: {mcp_data.get('DATE', 'N/A')}")
    print(f"Random Number: {mcp_data.get('RANDOM', 'N/A')}")
    print("----------------")

if __name__ == "__main__":
    view_mcp()
