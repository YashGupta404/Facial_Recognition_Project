# 🎯 Facial Recognition Attendance System

A modern web-based facial recognition attendance system built with React, FastAPI, and Supabase.

![Dashboard Preview](docs/dashboard.png)

## 🚀 Features

- **Face Registration** - Register user faces using browser webcam
- **Face Recognition** - Mark attendance automatically using face detection
- **User Management** - Complete CRUD operations for managing students
- **Attendance Tracking** - View, filter, and export attendance records
- **Real-time Stats** - Dashboard with live attendance statistics
- **Modern UI** - Beautiful dark theme with glassmorphism effects

## 🛠️ Tech Stack

### Frontend
- **React** + Vite
- **face-api.js** - Browser-based face detection & recognition
- **React Router** - Client-side routing
- **Lucide React** - Beautiful icons
- **React Webcam** - Webcam integration

### Backend
- **FastAPI** - Modern Python web framework
- **Supabase** - PostgreSQL database & authentication
- **Uvicorn** - ASGI server

### Deployment
- **Frontend**: Vercel
- **Backend**: Render.com
- **Database**: Supabase

## 📋 Prerequisites

- Node.js 18+
- Python 3.10+
- Supabase Account
- Git

## 🏃 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/facial-recognition-project.git
cd facial-recognition-project
```

### 2. Setup Supabase

1. Create a project at [supabase.com](https://supabase.com)
2. Run the SQL from `database/schema.sql` in the SQL Editor
3. Copy your project URL and API keys

### 3. Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Supabase credentials

# Run development server
uvicorn app.main:app --reload
```

### 4. Setup Frontend

```bash
cd frontend

# Install dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env if needed

# Run development server
npm run dev
```

### 5. Open the App

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/docs

## 🚀 Deployment

### Deploy Backend to Render

1. Go to [render.com](https://render.com) and sign up
2. Create a new Web Service
3. Connect your GitHub repository
4. Select the `backend` folder as root directory
5. Set environment variables:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
   - `SUPABASE_SERVICE_KEY`
   - `FRONTEND_URL` (your Vercel URL)
6. Deploy!

### Deploy Frontend to Vercel

1. Go to [vercel.com](https://vercel.com) and sign up
2. Import your GitHub repository
3. Select the `frontend` folder as root directory
4. Set environment variable:
   - `VITE_API_URL` (your Render backend URL)
5. Deploy!

## 📁 Project Structure

```
facial-recognition-project/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py          # Settings
│   │   ├── database.py        # Supabase connection
│   │   ├── main.py            # FastAPI app
│   │   ├── models.py          # Pydantic models
│   │   └── routes/
│   │       ├── users.py       # User endpoints
│   │       └── attendance.py  # Attendance endpoints
│   ├── requirements.txt
│   ├── Procfile
│   └── .env.example
│
├── frontend/
│   ├── public/
│   │   └── models/            # face-api.js models
│   ├── src/
│   │   ├── components/
│   │   │   └── Navbar.jsx
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── UsersPage.jsx
│   │   │   ├── RegisterFace.jsx
│   │   │   ├── RecognizeFace.jsx
│   │   │   └── AttendancePage.jsx
│   │   ├── services/
│   │   │   └── api.js         # API integration
│   │   ├── App.jsx
│   │   └── index.css
│   └── package.json
│
└── README.md
```

## 📝 API Endpoints

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users/` | Get all users |
| POST | `/api/users/` | Create new user |
| GET | `/api/users/{id}` | Get user by ID |
| PUT | `/api/users/{id}` | Update user |
| DELETE | `/api/users/{id}` | Delete user |
| POST | `/api/users/{id}/face-encoding` | Save face data |

### Attendance
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/attendance/` | Get all attendance |
| POST | `/api/attendance/mark` | Mark attendance |
| GET | `/api/attendance/today` | Today's attendance |
| GET | `/api/attendance/stats/today` | Today's stats |

## 🔐 Security Notes

- Never commit `.env` files
- Keep `SUPABASE_SERVICE_KEY` secret
- Enable Row Level Security (RLS) in production
- Use HTTPS in production

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [face-api.js](https://github.com/justadudewhohacks/face-api.js) for browser face detection
- [FastAPI](https://fastapi.tiangolo.com/) for the awesome framework
- [Supabase](https://supabase.com/) for the database platform
