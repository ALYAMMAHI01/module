
import datetime
import random

def generate_mcp():
    """Generates an MCP file with the current date and a random number."""
    date = datetime.date.today().isoformat()
    random_number = random.randint(0, 1000)
    with open("output.mcp", "w") as f:
        f.write(f"DATE: {date}\n")
        f.write(f"RANDOM: {random_number}\n")

if __name__ == "__main__":
    generate_mcp()
