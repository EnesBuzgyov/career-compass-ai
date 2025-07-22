# -*- coding: utf-8 -*-
"""
Simple script to configure .env file with Supabase connection details
"""

import re

def main():
    print("Supabase Database Configuration Helper")
    print("=" * 50)
    
    print("\nPlease provide your Supabase connection URL.")
    print("You can find this in your Supabase dashboard:")
    print("Settings -> Database -> Connection string -> URI")
    print("\nIt should look like:")
    print("postgresql://postgres:[YOUR-PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres")
    
    connection_url = input("\nEnter your Supabase connection URL: ").strip()
    
    if not connection_url:
        print("Please enter a valid connection URL")
        return
    
    # Parse the URL
    pattern = r'postgresql://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)'
    match = re.match(pattern, connection_url)
    
    if not match:
        print("Invalid PostgreSQL connection URL format")
        return
    
    user, password, host, port, database = match.groups()
    
    # Update .env file
    env_content = """# Database Configuration
POSTGRES_DB={}
POSTGRES_USER={}
POSTGRES_PASSWORD={}
POSTGRES_HOST={}
POSTGRES_PORT={}

# API Configuration
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACE_API_TOKEN=your_huggingface_token_here

# Application Settings
DEBUG=True
SECRET_KEY=your_secret_key_here""".format(database, user, password, host, port)
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("\n✅ .env file updated successfully!")
    print("\nDatabase configuration:")
    print("  POSTGRES_DB={}".format(database))
    print("  POSTGRES_USER={}".format(user))
    print("  POSTGRES_PASSWORD=***hidden***")
    print("  POSTGRES_HOST={}".format(host))
    print("  POSTGRES_PORT={}".format(port))
    
    print("\nNext steps:")
    print("1. Run: python setup_database.py")
    print("2. Test connection")

if __name__ == "__main__":
    main()
