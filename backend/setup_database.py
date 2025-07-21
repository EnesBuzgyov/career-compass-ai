#!/usr/bin/env python3
"""
Database setup script for Career Compass AI
Creates PostgreSQL database with pgvector extension and initial tables
"""

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_database():
    """Create the main database if it doesn't exist"""
    # Connect to PostgreSQL server (not specific database)
    try:
        conn = psycopg2.connect(
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            database="postgres"  # Connect to default postgres database
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        db_name = os.getenv("POSTGRES_DB", "career_compass_ai")
        
        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (db_name,))
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(f'CREATE DATABASE "{db_name}"')
            print(f"✅ Created database: {db_name}")
        else:
            print(f"✅ Database {db_name} already exists")
            
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        return False
    
    return True

def setup_pgvector():
    """Enable pgvector extension and create initial tables"""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "career_compass_ai"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432")
        )
        cursor = conn.cursor()
        
        # Enable pgvector extension
        cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        print("✅ Enabled pgvector extension")
        
        # Create resumes table with vector embeddings
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS resumes (
            id SERIAL PRIMARY KEY,
            text TEXT NOT NULL,
            label VARCHAR(255),
            job_title VARCHAR(255),
            skills TEXT[],
            experience_years INTEGER,
            education_level VARCHAR(100),
            embedding vector(384),  -- sentence-transformers/all-MiniLM-L6-v2 produces 384-dim vectors
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        cursor.execute(create_table_sql)
        print("✅ Created resumes table")
        
        # Create index for vector similarity search
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS resumes_embedding_idx 
            ON resumes USING ivfflat (embedding vector_cosine_ops) 
            WITH (lists = 100);
        """)
        print("✅ Created vector similarity index")
        
        # Create users table for future authentication
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            name VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        cursor.execute(create_users_table)
        print("✅ Created users table")
        
        # Create career_advice_sessions table
        create_sessions_table = """
        CREATE TABLE IF NOT EXISTS career_advice_sessions (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            resume_text TEXT,
            advice_response JSONB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        cursor.execute(create_sessions_table)
        print("✅ Created career_advice_sessions table")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("🎉 Database setup completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error setting up pgvector: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Career Compass AI database...")
    
    # Check if PostgreSQL is running
    try:
        conn = psycopg2.connect(
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            database="postgres"
        )
        conn.close()
        print("✅ PostgreSQL connection successful")
    except Exception as e:
        print(f"❌ Cannot connect to PostgreSQL: {e}")
        print("Please ensure PostgreSQL is installed and running.")
        print("Install PostgreSQL: https://www.postgresql.org/download/")
        return
    
    # Create database
    if not create_database():
        return
    
    # Setup pgvector and tables
    if not setup_pgvector():
        return
    
    print("\n🎯 Next steps:")
    print("1. Install new Python dependencies: pip install -r requirements.txt")
    print("2. Download and process the Kaggle Resume Dataset")
    print("3. Generate embeddings using sentence-transformers")

if __name__ == "__main__":
    main()
