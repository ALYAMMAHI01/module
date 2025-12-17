import sqlite3

def view_sql_database_tables(db_file):
    """
    Function to view all tables and their contents in a SQLite database.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Get all table names from sqlite_master
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print(f"No tables found in database: {db_file}")
            return

        print(f"Database: {db_file}")
        print("=" * 60)

        # Loop through each table
        for table in tables:
            table_name = table[0]
            print(f"\nTable: {table_name}")
            print("-" * 40)

            # Get table schema (column information)
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

            print("Columns:")
            for col in columns:
                col_id, col_name, col_type, not_null, default_val, pk = col
                pk_str = " (PRIMARY KEY)" if pk else ""
                print(f"  {col_name}: {col_type}{pk_str}")

            # Get all data from the table
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            print(f"\nData ({len(rows)} rows):")
            if rows:
                # Print column headers
                col_names = [col[1] for col in columns]
                header = " | ".join(col_names)
                print(header)
                print("-" * len(header))

                # Print each row
                for row in rows:
                    row_str = " | ".join(str(cell) if cell is not None else "NULL" for cell in row)
                    print(row_str)
            else:
                print("  (No data in this table)")

            print()

    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")

    finally:
        if conn:
            conn.close()

# Example usage

    # Database file name
    database_file = 'saeed_module4_1.db'

    # View all tables in the database
    view_sql_database_tables(database_file)
