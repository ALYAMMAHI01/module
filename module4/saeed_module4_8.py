import sqlite3

DB_NAME = 'saeed_module4_1.db'

def search_tasks_by_description(search_term):
    """
    Search for tasks where the description contains the search term (letters or numbers).
    Returns the best matching rows from the tasks table, searching only in the description column.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Use LIKE for partial matches in description
        query = "SELECT * FROM tasks WHERE description LIKE ?"
        cursor.execute(query, ('%' + search_term + '%',))

        rows = cursor.fetchall()

        return rows

    except sqlite3.Error as e:
        print(f"Error searching database: {e}")
        return []

    finally:
        if conn:
            conn.close()

