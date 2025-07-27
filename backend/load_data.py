#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data loading script for Career Compass AI
Reads resume data from a CSV file, generates embeddings, and inserts into the database.
"""

import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import numpy as np
from pgvector.psycopg2 import register_vector

# --- Configuration ---
# This section centralizes key settings for the script.

# We load environment variables from a .env file. This is a best practice
# for managing sensitive information like database credentials, keeping them
# separate from the source code.
# os.path.join ensures the path is correct regardless of the operating system.
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

# We specify the pre-trained model from sentence-transformers to use for creating embeddings.
# 'all-MiniLM-L6-v2' is a great general-purpose model: it's fast, lightweight, and provides
# high-quality embeddings for tasks like semantic search and clustering.
MODEL_NAME = 'all-MiniLM-L6-v2'

# --- Helper Functions ---
# Helper functions encapsulate reusable logic, making the main script cleaner.

def get_db_connection():
    """Establishes and returns a connection to the PostgreSQL database.
    
    This function reads the full database connection URL from the environment
    variables. Using a single URL is often more convenient than managing
    individual parts (host, user, password, etc.) separately.
    Returns:
        psycopg2.connection: A connection object to the database, or None if connection fails.
    """
    try:
        # Retrieve the connection string from environment variables.
        db_url = os.getenv("POSTGRES_URL")
        if not db_url:
            # Fail fast if the URL isn't configured, with a clear error message.
            raise Exception("POSTGRES_URL environment variable not set.")
        
        # Establish the connection using the psycopg2 library.
        conn = psycopg2.connect(db_url)
        return conn
    except Exception as e:
        # Catch any connection errors and print a descriptive message.
        print(f"❌ Database connection failed: {e}")
        return None

def show_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    """Displays a simple, dynamic progress bar in the console.

    This is a user-friendly feature to provide visual feedback for long-running processes,
    like iterating through thousands of resumes.
    Args:
        iteration (int): The current iteration number.
        total (int): The total number of iterations.
        prefix (str): Text to display before the progress bar.
        suffix (str): Text to display after the progress bar.
        length (int): The character length of the progress bar.
        fill (str): The character used to fill the progress bar.
    """
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    # The '\r' (carriage return) moves the cursor to the beginning of the line,
    # so each update overwrites the previous one, creating a dynamic effect.
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    # Print a newline character when the loop is complete.
    if iteration == total:
        print()

# --- Main Logic ---
# The main() function is the primary entry point for the script's execution.

def main():
    """Main function to orchestrate the loading and processing of resume data."""
    print("🚀 Starting data loading process...")

    # Step 1: Load the dataset from the CSV file.
    # We construct the path relative to the script's location to ensure it works
    # regardless of where the script is called from.
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'UpdatedResumeDataSet.csv')
    try:
        # pandas.read_csv is a powerful function for reading tabular data.
        df = pd.read_csv(data_path)
        print(f"✅ Successfully loaded {len(df)} resumes from CSV.")
    except FileNotFoundError:
        # If the file doesn't exist, provide a helpful message to the user.
        print(f"❌ Error: The file was not found at {data_path}")
        print("Please ensure you have downloaded the dataset and placed it in the 'backend/data' directory.")
        return # Exit the script if the data isn't available.

    # Step 2: Initialize the sentence transformer model.
    # The model is downloaded from the Hugging Face Hub the first time it's used
    # and cached locally for subsequent runs.
    print(f"🤖 Loading sentence transformer model: '{MODEL_NAME}'...")
    model = SentenceTransformer(MODEL_NAME)
    print("✅ Model loaded.")

    # Step 3: Connect to the database.
    print("🗄️ Connecting to the database...")
    conn = get_db_connection()
    if conn is None:
        # If the connection fails, the helper function will have printed an error.
        # We exit the script gracefully.
        return
    
    # Register the vector type adapter with the connection. This teaches psycopg2
    # how to handle numpy arrays when inserting them into 'vector' columns.
    register_vector(conn)
    
    cursor = conn.cursor()
    print("✅ Database connection successful.")

    # Step 4: Clear existing data for a clean import.
    # TRUNCATE is faster than DELETE for clearing an entire table.
    # RESTART IDENTITY resets the auto-incrementing primary key, so the new data starts from ID 1.
    print("🧹 Clearing existing data from the 'resumes' table...")
    cursor.execute("TRUNCATE TABLE resumes RESTART IDENTITY;")
    print("✅ Table cleared.")

    # Step 5: Process each resume and insert it into the database.
    print("⏳ Processing resumes and generating embeddings...")
    total_resumes = len(df)
    # Initialize the progress bar before starting the loop.
    show_progress_bar(0, total_resumes, prefix='Progress:', suffix='Complete', length=50)

    # We iterate over each row in the DataFrame using df.iterrows().
    for i, row in df.iterrows():
        try:
            # Extract the relevant data from the current row.
            category = row['Category']
            resume_text = row['Resume']

            # This is the core of the AI functionality: converting text to a numerical vector.
            # The .encode() method takes the text and returns a NumPy array representing the embedding.
            embedding = model.encode(resume_text)

            # Execute the SQL INSERT statement.
            # We use parameterized queries (with %s) to prevent SQL injection vulnerabilities.
            # The registered adapter now correctly handles the numpy array for the vector column.
            cursor.execute(
                "INSERT INTO resumes (category, resume_text, embedding) VALUES (%s, %s, %s)",
                (category, resume_text, embedding)
            )
            
            # Update the progress bar after each successful insertion.
            show_progress_bar(i + 1, total_resumes, prefix='Progress:', suffix='Complete', length=50)

        except Exception as e:
            # If an error occurs for a specific resume, we print the error, rollback the
            # current transaction, and continue to the next resume.
            # This makes the script more resilient to issues with individual data points.
            print(f"\n❌ Error processing row {i}: {e}")
            conn.rollback() # Rollback the transaction on error
            continue # Continue with the next row

    # After the loop finishes, we commit the entire transaction to save all changes.
    conn.commit()
    cursor.close()
    conn.close()

    print("\n🎉 Data loading process completed successfully!")
    print(f"✅ Inserted {total_resumes} resumes into the database.")

# This is standard Python practice. The code inside this block will only run
# when the script is executed directly (e.g., `python3 load_data.py`),
# not when it's imported as a module into another script.
if __name__ == "__main__":
    main()
