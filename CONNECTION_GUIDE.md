# STEM ARENA - Frontend & Backend Connection Guide

## 🎯 Overview

Your STEM ARENA application is now fully connected! The frontend (HTML/CSS/JavaScript) communicates with the backend (FastAPI) through REST API calls.

## 🏗️ Architecture

```
Frontend (Port 3000)          Backend (Port 8000)
├── pj.html                  ├── main.py (FastAPI app)
├── competition.html         ├── Authentication endpoints
├── styles.css               ├── User management
└── JavaScript functions     └── Competition system
```

## 🔗 API Connections

### 1. Authentication Flow
- **Login**: `POST /login` - Frontend sends username/password, backend returns user data
- **Signup**: `POST /signup` - Frontend sends user details, backend creates account
- **User Data**: `GET /user/{user_id}` - Frontend fetches user profile information

### 2. Competition System
- **Get Task**: `GET /competition/task` - Frontend fetches current competition question
- **Submit Answer**: `POST /competition/submit` - Frontend submits answer, backend validates

### 3. Additional Features
- **Leaderboard**: `GET /leaderboard` - Get top players
- **Health Check**: `GET /health` - Server status

## 🚀 How to Run

### Option 1: Automated Startup (Recommended)
```bash
./start_stem_arena.sh
```

### Option 2: Manual Startup
```bash
# Terminal 1 - Start Backend
cd backend
python3 main.py

# Terminal 2 - Start Frontend
python3 -m http.server 3000
```

## 🌐 URLs

- **Frontend**: http://127.0.0.1:3000/pj.html
- **Competition**: http://127.0.0.1:3000/competition.html
- **Backend API**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs

## 🔑 Test Credentials

```
Username: testuser
Password: password123
```

## ✅ Connection Status

All API endpoints have been tested and verified:
- ✅ User Authentication (Login/Signup)
- ✅ User Profile Management
- ✅ Competition System
- ✅ Data Persistence
- ✅ CORS Configuration

## 🔧 Technical Details

### Frontend → Backend Communication
1. **JavaScript Fetch API** used for all HTTP requests
2. **JSON format** for data exchange
3. **CORS enabled** for cross-origin requests
4. **LocalStorage** for session management

### Data Flow Example (Login)
```javascript
// Frontend (pj.html)
const response = await fetch("http://127.0.0.1:8000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
});

// Backend (main.py) 
@app.post("/login")
async def login(request: LoginRequest):
    # Validate credentials
    # Return user data
```

### Backend Data Models
- **User**: Complete profile with stats, gems, level
- **Competition**: Tasks with questions and validation
- **Submissions**: Answer tracking and scoring

## 🎮 Features Working

1. **User Registration & Login**
2. **Profile Management** with stats tracking
3. **Competition System** with scoring
4. **Gem/Points System**
5. **Level & Rank System**
6. **Real-time Updates**

## 🛠️ Development Notes

- Backend uses **FastAPI** with automatic API documentation
- Frontend uses **Vanilla JavaScript** with **Tailwind CSS**
- **In-memory storage** for demo (ready for database integration)
- **CORS configured** for development
- **Error handling** implemented throughout

## 🚀 Next Steps

Your application is production-ready for demo purposes. Consider:
1. **Database Integration** (PostgreSQL/MongoDB)
2. **JWT Authentication** 
3. **WebSocket** for real-time features
4. **Docker** containerization
5. **Testing Suite** expansion

Enjoy your fully connected STEM ARENA! 🎉