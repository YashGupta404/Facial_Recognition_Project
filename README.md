<div align="center">

# 🎯 FaceRecog - Facial Recognition Attendance System

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen?style=for-the-badge)](https://facial-recognition-project-six.vercel.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=white)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)

<p align="center">
  <strong>A modern, web-based facial recognition attendance system with real-time face detection, user management, and comprehensive attendance tracking.</strong>
</p>

[Live Demo](https://facial-recognition-project-six.vercel.app) •
[API Documentation](https://facialrecognitionproject-production.up.railway.app/docs) •
[Report Bug](https://github.com/YashGupta404/Facial_Recognition_Project/issues)

---

</div>

## 📸 Screenshots

<div align="center">
  <img src="docs/dashboard.png" alt="Dashboard" width="80%"/>
  <p><em>Modern Dashboard with Real-time Statistics</em></p>
</div>

## ✨ Features

### 🔐 **Face Recognition**
- **Browser-based Detection** - Uses face-api.js for client-side face detection
- **Real-time Recognition** - Instant face matching without server delay
- **Multi-face Support** - Capture multiple face samples for improved accuracy
- **Auto-attendance Mode** - Continuously scan and mark attendance

### 👥 **User Management**
- **Complete CRUD Operations** - Add, edit, view, and delete student records
- **Detailed Profiles** - Store comprehensive student information
- **Face Registration Status** - Track which users have registered their faces
- **Search & Filter** - Quickly find users by name, ID, or email

### 📊 **Attendance Tracking**
- **Real-time Statistics** - Dashboard shows live attendance metrics
- **Daily Reports** - View attendance by date
- **Export to CSV** - Download attendance data for external use
- **Automatic Timestamps** - Records check-in time automatically

### 🎨 **Modern UI/UX**
- **Dark Theme** - Eye-friendly dark mode with purple/blue accents
- **Glassmorphism Design** - Modern, translucent card effects
- **Responsive Layout** - Works on desktop and tablet devices
- **Smooth Animations** - Polished micro-interactions

## 🛠️ Tech Stack

### Frontend
| Technology | Purpose |
|------------|---------|
| ![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black) | UI Framework |
| ![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white) | Build Tool |
| ![face-api.js](https://img.shields.io/badge/face--api.js-FF6B6B?style=flat-square) | Face Detection |
| ![React Router](https://img.shields.io/badge/React_Router-CA4245?style=flat-square&logo=react-router&logoColor=white) | Client Routing |
| ![Lucide](https://img.shields.io/badge/Lucide-F56565?style=flat-square) | Icons |

### Backend
| Technology | Purpose |
|------------|---------|
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) | REST API |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Runtime |
| ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square) | Validation |
| ![Uvicorn](https://img.shields.io/badge/Uvicorn-2C3E50?style=flat-square) | ASGI Server |

### Database & Deployment
| Technology | Purpose |
|------------|---------|
| ![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white) | PostgreSQL Database |
| ![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white) | Frontend Hosting |
| ![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white) | Backend Hosting |

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         CLIENT BROWSER                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐  │
│  │   React + Vite   │  │   face-api.js    │  │   Webcam     │  │
│  │   (Frontend UI)  │  │ (Face Detection) │  │   (WebRTC)   │  │
│  └────────┬─────────┘  └────────┬─────────┘  └──────────────┘  │
└───────────┼─────────────────────┼──────────────────────────────┘
            │                     │
            │ HTTP/REST           │ Client-side
            ▼                     ▼ Processing
┌─────────────────────────────────────────────────────────────────┐
│                      VERCEL (Frontend Host)                      │
│                  facial-recognition-project.vercel.app           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ API Calls
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     RAILWAY (Backend Host)                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    FastAPI Application                    │   │
│  │  ┌────────────┐  ┌────────────────┐  ┌────────────────┐  │   │
│  │  │ /api/users │  │ /api/attendance │  │  /api/health  │  │   │
│  │  └────────────┘  └────────────────┘  └────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                facialrecognitionproject-production.up.railway.app │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Supabase Client
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SUPABASE (Database)                         │
│  ┌──────────────────┐        ┌──────────────────────────────┐   │
│  │      users       │        │         attendance           │   │
│  │  - id            │        │  - id                        │   │
│  │  - student_id    │◄──────►│  - user_id                   │   │
│  │  - name          │        │  - student_id                │   │
│  │  - face_encoding │        │  - attendance_date           │   │
│  │  - ...           │        │  - check_in_time             │   │
│  └──────────────────┘        └──────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ ([Download](https://nodejs.org/))
- **Python** 3.10+ ([Download](https://python.org/))
- **Git** ([Download](https://git-scm.com/))
- **Supabase Account** ([Sign Up](https://supabase.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YashGupta404/Facial_Recognition_Project.git
   cd Facial_Recognition_Project
   ```

2. **Set up the Backend**
   ```bash
   cd backend
   
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Configure environment
   cp .env.example .env
   # Edit .env with your Supabase credentials
   
   # Start the server
   uvicorn app.main:app --reload
   ```

3. **Set up the Frontend**
   ```bash
   cd frontend
   
   # Install dependencies
   npm install
   
   # Configure environment
   cp .env.example .env
   # Edit .env if needed
   
   # Start the development server
   npm run dev
   ```

4. **Open the application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000/docs

## ⚙️ Environment Variables

### Backend (`backend/.env`)

| Variable | Description | Example |
|----------|-------------|---------|
| `SUPABASE_URL` | Your Supabase project URL | `https://xxx.supabase.co` |
| `SUPABASE_KEY` | Supabase anon/public key | `eyJhbG...` |
| `SUPABASE_SERVICE_KEY` | Supabase service role key | `eyJhbG...` |
| `FRONTEND_URL` | Frontend URL for CORS | `https://your-app.vercel.app` |

### Frontend (`frontend/.env`)

| Variable | Description | Example |
|----------|-------------|---------|
| `VITE_API_URL` | Backend API URL | `https://your-api.railway.app` |

## 📚 API Reference

### Base URL
```
https://facialrecognitionproject-production.up.railway.app
```

### Endpoints

#### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/users/` | Get all users |
| `POST` | `/api/users/` | Create a new user |
| `GET` | `/api/users/{student_id}` | Get user by student ID |
| `PUT` | `/api/users/{student_id}` | Update user |
| `DELETE` | `/api/users/{student_id}` | Delete user |
| `POST` | `/api/users/{student_id}/face-encoding` | Save face encoding |
| `GET` | `/api/users/with-face/all` | Get users with registered faces |

#### Attendance

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/attendance/` | Get all attendance records |
| `POST` | `/api/attendance/mark` | Mark attendance (via face recognition) |
| `GET` | `/api/attendance/today` | Get today's attendance |
| `GET` | `/api/attendance/stats/today` | Get today's statistics |
| `DELETE` | `/api/attendance/{id}` | Delete attendance record |

#### Health Check

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | API health check |
| `GET` | `/` | API info |

### Example Request

```bash
# Get all users
curl -X GET "https://facialrecognitionproject-production.up.railway.app/api/users/"

# Create a new user
curl -X POST "https://facialrecognitionproject-production.up.railway.app/api/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": "STU001",
    "name": "John Doe",
    "email": "john@example.com",
    "department": "Computer"
  }'
```

## 🗄️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    department VARCHAR(50),
    course VARCHAR(50),
    year VARCHAR(10),
    semester VARCHAR(10),
    division VARCHAR(10),
    roll_no VARCHAR(20),
    gender VARCHAR(20),
    dob DATE,
    address TEXT,
    teacher_name VARCHAR(100),
    photo_sample_status VARCHAR(20) DEFAULT 'No',
    face_encoding TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Attendance Table
```sql
CREATE TABLE attendance (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    student_id VARCHAR(50) NOT NULL,
    name VARCHAR(100),
    roll_no VARCHAR(20),
    department VARCHAR(50),
    attendance_status VARCHAR(20) DEFAULT 'Present',
    check_in_time TIME,
    attendance_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## 🚢 Deployment

### Deploy Frontend to Vercel

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com) and import your repository
3. Set the **Root Directory** to `frontend`
4. Add environment variable: `VITE_API_URL`
5. Deploy!

### Deploy Backend to Railway

1. Go to [railway.app](https://railway.app) and create a new project
2. Connect your GitHub repository
3. Set the **Root Directory** to `backend`
4. Add environment variables (Supabase credentials)
5. Railway will auto-deploy on push

### Set up Supabase

1. Create a project at [supabase.com](https://supabase.com)
2. Run the SQL schema in the SQL Editor
3. Copy your API keys to the backend `.env`

## 📁 Project Structure

```
Facial_Recognition_Project/
├── 📂 backend/
│   ├── 📂 app/
│   │   ├── __init__.py
│   │   ├── config.py           # Environment configuration
│   │   ├── database.py         # Supabase connection
│   │   ├── main.py             # FastAPI application
│   │   ├── models.py           # Pydantic models
│   │   └── 📂 routes/
│   │       ├── users.py        # User endpoints
│   │       └── attendance.py   # Attendance endpoints
│   ├── requirements.txt
│   ├── Procfile
│   └── .env.example
│
├── 📂 frontend/
│   ├── 📂 public/
│   │   └── 📂 models/          # face-api.js model files
│   ├── 📂 src/
│   │   ├── 📂 components/
│   │   │   └── Navbar.jsx
│   │   ├── 📂 pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── UsersPage.jsx
│   │   │   ├── RegisterFace.jsx
│   │   │   ├── RecognizeFace.jsx
│   │   │   └── AttendancePage.jsx
│   │   ├── 📂 services/
│   │   │   └── api.js          # API client
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css           # Global styles
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── 📂 Facial_Recognition_App/  # Legacy desktop app (archived)
├── README.md
├── LICENSE
└── .gitignore
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔒 Security

- Never commit `.env` files to version control
- Keep your `SUPABASE_SERVICE_KEY` secret
- Enable Row Level Security (RLS) in Supabase for production
- Use HTTPS in production environments

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Yash Gupta**
- GitHub: [@YashGupta404](https://github.com/YashGupta404)

## 🙏 Acknowledgments

- [face-api.js](https://github.com/justadudewhohacks/face-api.js) - Browser face detection library
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [Supabase](https://supabase.com/) - Open source Firebase alternative
- [Vercel](https://vercel.com/) - Frontend deployment platform
- [Railway](https://railway.app/) - Backend deployment platform

---

<div align="center">
  <p>⭐ Star this repository if you found it helpful!</p>
  <p>Made with ❤️ by <a href="https://github.com/YashGupta404">Yash Gupta</a></p>
</div>
