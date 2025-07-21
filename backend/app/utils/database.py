import os
import psycopg2
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import numpy as np
from typing import List, Optional, Tuple

# Load environment variables from .env file
load_dotenv()

# Database configuration
DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER', 'postgres')}:{os.getenv('POSTGRES_PASSWORD', 'postgres')}@{os.getenv('POSTGRES_HOST', 'localhost')}:{os.getenv('POSTGRES_PORT', '5432')}/{os.getenv('POSTGRES_DB', 'career_compass_ai')}"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_connection():
    """
    Create a connection to PostgreSQL database using environment variables.
    Will be used for future pgvector operations.
    """
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "career_compass_ai"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432")
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def get_db_session():
    """
    Get SQLAlchemy database session
    """
    return SessionLocal()

def insert_resume(text: str, label: str, job_title: str, skills: List[str], 
                 experience_years: int, education_level: str, embedding: np.ndarray) -> Optional[int]:
    """
    Insert a resume with its vector embedding into the database
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        insert_sql = """
        INSERT INTO resumes (text, label, job_title, skills, experience_years, education_level, embedding)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """
        
        cursor.execute(insert_sql, (
            text, label, job_title, skills, experience_years, education_level, embedding.tolist()
        ))
        
        resume_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        
        return resume_id
        
    except Exception as e:
        print(f"Error inserting resume: {e}")
        return None

def similarity_search(query_embedding: np.ndarray, limit: int = 5) -> List[Tuple]:
    """
    Perform vector similarity search to find similar resumes
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        search_sql = """
        SELECT id, text, label, job_title, skills, experience_years, education_level,
               embedding <=> %s AS distance
        FROM resumes
        ORDER BY embedding <=> %s
        LIMIT %s;
        """
        
        cursor.execute(search_sql, (query_embedding.tolist(), query_embedding.tolist(), limit))
        results = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return results
        
    except Exception as e:
        print(f"Error in similarity search: {e}")
        return []

def get_resume_count() -> int:
    """
    Get total number of resumes in the database
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM resumes;")
        count = cursor.fetchone()[0]
        
        cursor.close()
        conn.close()
        
        return count
        
    except Exception as e:
        print(f"Error getting resume count: {e}")
        return 0

def test_connection() -> bool:
    """
    Test database connection and pgvector extension
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Test basic connection
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        print(f"PostgreSQL version: {version}")
        
        # Test pgvector extension
        cursor.execute("SELECT extname FROM pg_extension WHERE extname = 'vector';")
        vector_ext = cursor.fetchone()
        
        if vector_ext:
            print("✅ pgvector extension is installed")
        else:
            print("❌ pgvector extension not found")
            return False
        
        cursor.close()
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"Database connection test failed: {e}")
        return False
