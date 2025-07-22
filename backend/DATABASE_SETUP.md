# Database Setup Options for Career Compass AI

## Option 1: Supabase (Recommended - Free & Fast)

1. **Sign up at [supabase.com](https://supabase.com)**
2. **Create a new project**
   - Choose any name (e.g., "career-compass-ai")
   - Select a region close to you
   - Generate a strong password
3. **Get connection details**
   - Go to Settings → Database
   - Copy the connection string
4. **pgvector is already enabled!** ✅

### Connection String Format:
```
postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT-REF].supabase.co:5432/postgres
```

## Option 2: Neon (Alternative Free Option)

1. **Sign up at [neon.tech](https://neon.tech)**
2. **Create a database**
3. **Enable pgvector** (may require manual setup)

## Option 3: Railway (Another Alternative)

1. **Sign up at [railway.app](https://railway.app)**
2. **Deploy PostgreSQL template**
3. **Add pgvector extension**

## Quick Setup Instructions

Once you have your database URL:

1. **Update your .env file:**
```bash
# Copy .env.example to .env
cp .env.example .env

# Edit .env with your database URL
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password_here
POSTGRES_HOST=your_host_here
POSTGRES_PORT=5432
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run database setup:**
```bash
python setup_database.py
```

4. **Test connection:**
```bash
python -c "from app.utils.database import test_connection; test_connection()"
```

## What Gets Created

The setup script will create:
- ✅ `resumes` table with vector embeddings (384 dimensions)
- ✅ `users` table for authentication
- ✅ `career_advice_sessions` table for storing advice history
- ✅ Vector similarity search indexes
- ✅ pgvector extension enabled

## Next Steps After Database Setup

1. Download Kaggle Resume Dataset
2. Generate embeddings using sentence-transformers
3. Populate the database with resume data
4. Test RAG functionality

---

**Recommendation:** Go with Supabase - it's the fastest to set up and has pgvector pre-enabled!
