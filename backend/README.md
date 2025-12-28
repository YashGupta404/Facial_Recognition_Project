# Facial Recognition API - Backend

This is the backend API for the Facial Recognition Attendance System.

## Tech Stack
- **FastAPI** - Modern Python web framework
- **Supabase** - PostgreSQL database & authentication
- **Uvicorn** - ASGI server

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your Supabase credentials

4. Run the development server:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Deployment

This backend is designed to be deployed on Render.com (free tier).
