
import datetime
import sqlite3
import os

DB_FILE = "mcp.db"

def initialize_database():
    """Initializes the SQLite database and populates it with sample data if it's new."""
    if os.path.exists(DB_FILE):
        return

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE information (
        id INTEGER PRIMARY KEY,
        key TEXT NOT NULL,
        value TEXT NOT NULL
    )
    """)

    sample_data = [
        ("System Status", "All systems operational."),
        ("Current User", "Jules"),
        ("Project Version", "1.1.0"),
        ("Last Check-in", "2024-07-31T10:00:00Z")
    ]
    cursor.executemany("INSERT INTO information (key, value) VALUES (?, ?)", sample_data)

    conn.commit()
    conn.close()
    print(f"Database '{DB_FILE}' created and populated.")

def generate_mcp():
    """Generates an MCP file with the current date and a random value from the database."""
    initialize_database()

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT key, value FROM information ORDER BY RANDOM() LIMIT 1")
    db_data = cursor.fetchone()
    conn.close()

    date = datetime.date.today().isoformat()
    
    with open("output.mcp", "w") as f:
        f.write(f"DATE: {date}\n")
        if db_data:
            f.write(f"{db_data[0]}: {db_data[1]}\n")
        else:
            f.write("DB_STATUS: No data found\n")


if __name__ == "__main__":
    generate_mcp()
