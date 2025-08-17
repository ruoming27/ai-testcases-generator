import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        cursor_factory=RealDictCursor
    )


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_cases (
            id SERIAL PRIMARY KEY,
            description TEXT,
            steps TEXT,
            expected_result TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


def save_test_case(description, steps, expected_result):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO test_cases (description, steps, expected_result)
        VALUES (%s, %s, %s)
    """, (description, steps, expected_result))
    conn.commit()
    cursor.close()
    conn.close()


def fetch_test_cases():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_cases")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
