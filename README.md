# Career Compass AI

A résumé-aware Gen-AI career-coach that analyzes your resume and provides tailored career advice.

## Overview

Career Compass AI is a web application that helps job seekers navigate their career paths effectively. By leveraging AI and machine learning, the system analyzes resumes against job market data to identify skill gaps, suggest improvements, and recommend optimal career paths.

## Technology Stack

### Frontend
- **Next.js 14**: React framework for building the user interface
- **Tailwind CSS**: Utility-first CSS framework for styling
- **TypeScript**: Static typing for improved development experience
- **Axios**: HTTP client for API communication

### Backend
- **FastAPI**: High-performance Python web framework for building APIs
- **LangChain**: Framework for developing applications powered by language models
- **PostgreSQL + pgvector**: Database with vector extensions for similarity search
- **Sentence Transformers**: For embedding generation
- **Hugging Face Transformers**: For accessing pre-trained language models

## Project Structure

```
career-compass-ai/
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── main.py        # Entry point for the FastAPI application
│   │   ├── routers/       # API route definitions
│   │   ├── models/        # Data models and schemas
│   │   ├── services/      # Business logic
│   │   └── utils/         # Utility functions
│   └── requirements.txt   # Python dependencies
│
├── frontend/              # Next.js frontend
│   ├── src/
│   │   ├── app/           # Next.js app directory
│   │   ├── components/    # Reusable UI components
│   │   ├── utils/         # Utility functions
│   │   └── styles/        # CSS and styling
│   ├── package.json       # Node.js dependencies
│   └── tailwind.config.js # Tailwind CSS configuration
│
└── Plan/                  # Project planning documents
```

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Run the development server:
   ```
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser to see the application.

## Features

- Resume upload and analysis
- Skills gap identification
- Career path recommendations
- Resume improvement suggestions

## Development Roadmap

### Week 1: Data & Infrastructure
- Set up database with pgvector
- Ingest resume dataset and create embeddings

### Week 2: RAG API
- Build LangChain chain for resume analysis
- Implement FastAPI endpoints

### Week 3: UI & Streaming
- Develop Next.js chat interface
- Add resume upload functionality
- Implement streaming responses

### Week 4: Fine-tuning & Polish
- Fine-tune models for better performance
- Add metrics tracking
- Deploy to production