#!/usr/bin/env python3
"""
Helper script to configure .env file with Supabase connection details
"""

import re
import os

def parse_supabase_url(connection_url):
    """Parse Supabase connection URL into components"""
    # Pattern: postgresql://postgres:password@db.project-ref.supabase.co:5432/postgres
    pattern = r'postgresql://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)'
    match = re.match(pattern, connection_url)
    
    if not match:
        raise ValueError("Invalid PostgreSQL connection URL format")
    
    user, password, host, port, database = match.groups()
    return {
        'POSTGRES_USER': user,
        'POSTGRES_PASSWORD': password,
        'POSTGRES_HOST': host,
        'POSTGRES_PORT': port,
        'POSTGRES_DB': database
    }

def update_env_file(db_config):
    """Update .env file with database configuration"""
    env_path = '.env'
    
    # Read current .env file
    with open(env_path, 'r') as f:
        lines = f.readlines()
    
    # Update database configuration
    updated_lines = []
    for line in lines:
        if line.startswith('POSTGRES_'):
            key = line.split('=')[0]
            if key in db_config:
                updated_lines.append("{}={}\n".format(key, db_config[key]))
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    
    # Write updated .env file
    with open(env_path, 'w') as f:
        f.writelines(updated_lines)
    
    print("✅ .env file updated successfully!")
    print("\nDatabase configuration:")
    for key, value in db_config.items():
        if 'PASSWORD' in key:
            print("  {}=***hidden***".format(key))
        else:
            print("  {}={}".format(key, value))

def main():
    print("🚀 Supabase Database Configuration Helper")
    print("=" * 50)
    
    print("\nPlease provide your Supabase connection URL.")
    print("You can find this in your Supabase dashboard:")
    print("Settings → Database → Connection string → URI")
    print("\nIt should look like:")
    print("postgresql://postgres:[YOUR-PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres")
    
    while True:
        connection_url = input("\nEnter your Supabase connection URL: ").strip()
        
        if not connection_url:
            print("❌ Please enter a valid connection URL")
            continue
        
        try:
            db_config = parse_supabase_url(connection_url)
            update_env_file(db_config)
            break
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Please check your connection URL format and try again.")
    
    print("\n🎯 Next steps:")
    print("1. Run: python setup_database.py")
    print("2. Test connection: python -c \"from app.utils.database import test_connection; test_connection()\"")

if __name__ == "__main__":
    main()
