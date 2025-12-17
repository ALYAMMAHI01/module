import sqlite3

def view_database_tables(db_name):
    """View all tables and their data in the SQLite database."""
    try:
        # Connect to the database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print(f"No tables found in database '{db_name}'")
            return

        print(f"Tables in database '{db_name}':")
        print("-" * 50)

        for table in tables:
            table_name = table[0]
            print(f"\nTable: {table_name}")

            # Get table schema
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

            print("Columns:")
            for col in columns:
                print(f"  - {col[1]} ({col[2]}) {'PRIMARY KEY' if col[5] else ''}")
            print()

            # Get table data
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            if rows:
                print("Data:")
                # Print column headers
                col_names = [col[1] for col in columns]
                print(" | ".join(col_names))
                print("-" * (len(" | ".join(col_names))))

                # Print data rows
                for row in rows:
                    print(" | ".join(str(cell) for cell in row))
            else:
                print("No data in this table.")

            print("-" * 50)

    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Database file name
    DB_NAME = 'saeed_module4_1.db'

    # View all tables and data
    view_database_tables(DB_NAME)