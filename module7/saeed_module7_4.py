
import psycopg2
from faker import Faker
import os
import time

def create_table(conn):
    """Creates the users table if it doesn't exist."""
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            phone VARCHAR(255),
            user_key VARCHAR(255)
        )
    """)
    conn.commit()
    cur.close()

fake = Faker()

def generate_user_data():
    """Generates a dictionary of random user data."""
    return {
        "name": fake.name(),
        "phone": fake.phone_number(),
        "user_key": fake.uuid4()
    }

def insert_user_data(conn, user_data):
    """Inserts a user record into the users table."""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, phone, user_key) VALUES (%s, %s, %s)",
        (user_data["name"], user_data["phone"], user_data["user_key"])
    )
    conn.commit()
    cur.close()

def main():
    while True:
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST", "db"),
                dbname=os.getenv("DB_NAME", "postgres"),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASSWORD", "postgres"),
                port=os.getenv("DB_PORT", "5432")
            )
            print("Database connection successful")
            create_table(conn)
            print("Table 'users' created or already exists.")

            for _ in range(10):
                user_data = generate_user_data()
                insert_user_data(conn, user_data)
                print(f"Inserted user: {user_data['name']}")

            conn.close()
            break
        except psycopg2.OperationalError:
            print("Database connection failed, retrying...")
            time.sleep(1)

if __name__ == "__main__":
    main()
