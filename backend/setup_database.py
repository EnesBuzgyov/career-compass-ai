#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Database setup script for Career Compass AI
Creates PostgreSQL database with pgvector extension and initial tables
"""

import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file in the same directory
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

def setup_pgvector():
    """Enable pgvector extension and create initial tables"""
    try:
        db_url = os.getenv("POSTGRES_URL")
        if not db_url:
            raise Exception("POSTGRES_URL environment variable not set.")

        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        
        # Enable pgvector extension
        cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        print("✅ Enabled pgvector extension")
        
        # Drop the table if it exists to ensure a clean slate with the correct schema.
        # CASCADE will also remove any dependent objects like indexes.
        cursor.execute("DROP TABLE IF EXISTS resumes CASCADE;")
        print("🧹 Dropped existing resumes table (if any) for a fresh start.")

        # Create resumes table with vector embeddings
        # This schema is simplified to match exactly what is in our Kaggle dataset and load script.
        # We can add more columns like skills, experience, etc., later as we build more features.
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS resumes (
            id SERIAL PRIMARY KEY,
            category VARCHAR(255) NOT NULL,
            resume_text TEXT NOT NULL,
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
        print("❌ Error setting up database: {}".format(e))
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Career Compass AI database on Supabase...")
    
    if not setup_pgvector():
        print("Aborting setup.")
        return
    
    print("\n🎯 Next steps:")
    print("1. Download and process the Kaggle Resume Dataset")
    print("2. Generate embeddings using sentence-transformers")
    print("3. Run the backend server: uvicorn app.main:app --reload")

if __name__ == "__main__":
    main()
