from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database file name (same as module4_1)
DB_NAME = 'saeed_module4_1.db'

def insert_tasks(tasks):
    """Insert multiple tasks into the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Prepare the insert statement
        insert_query = """
        INSERT INTO tasks (title, description, status)
        VALUES (?, ?, ?)
        """

        # Insert each task
        for task in tasks:
            cursor.execute(insert_query, (task['title'], task['description'], task['status']))

        conn.commit()
        return True, f"Successfully inserted {len(tasks)} tasks"

    except sqlite3.Error as e:
        return False, f"Error inserting tasks: {e}"

    finally:
        if conn:
            conn.close()

@app.route('/api/tasks', methods=['POST'])
def add_tasks():
    """POST endpoint to add 2 tasks to the database."""
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate that we have exactly 2 tasks
        if not data or 'tasks' not in data or len(data['tasks']) != 2:
            return jsonify({
                'error': 'Request must contain exactly 2 tasks in JSON format: {"tasks": [{"title": "...", "description": "...", "status": "..."}, {...}]}'
            }), 400

        tasks = data['tasks']

        # Validate each task has required fields
        for i, task in enumerate(tasks):
            if not all(key in task for key in ['title', 'description', 'status']):
                return jsonify({
                    'error': f'Task {i+1} is missing required fields. Each task must have title, description, and status.'
                }), 400

        # Insert the tasks
        success, message = insert_tasks(tasks)

        if success:
            return jsonify({
                'message': message,
                'tasks_added': len(tasks)
            }), 201
        else:
            return jsonify({'error': message}), 500

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


