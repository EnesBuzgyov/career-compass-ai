import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    """
    Create a connection to PostgreSQL database using environment variables.
    Will be used for future pgvector operations.
    """
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432")
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
