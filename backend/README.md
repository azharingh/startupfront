# STEM ARENA Backend

This is the backend server for the STEM ARENA competition platform.

## Features

- ✅ User Authentication (Login/Signup)
- ✅ User Profile Management
- ✅ Competition Task Management
- ✅ Solution Submission & Scoring
- ✅ Leaderboard System
- ✅ CORS enabled for frontend communication
- ✅ Interactive API documentation

## Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python start_server.py
```

Or alternatively:

```bash
python main.py
```

### 3. Access the API

- **Server**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs
- **Alternative Docs**: http://127.0.0.1:8000/redoc

## API Endpoints

### Authentication
- `POST /login` - User login
- `POST /signup` - User registration

### User Management
- `GET /user/{user_id}` - Get user profile

### Competitions
- `GET /competition/task` - Get current competition task
- `POST /competition/submit` - Submit solution

### Additional
- `GET /leaderboard` - Get top users
- `GET /health` - Health check

## Test User

For testing, use these credentials:
- **Username**: `testuser`
- **Password**: `password123`

## Frontend Integration

The backend is configured to work with the STEM ARENA frontend. Make sure your frontend is making requests to `http://127.0.0.1:8000`.

## Development Notes

- Uses in-memory storage (replace with database in production)
- Passwords are stored in plain text (implement hashing in production)
- JWT tokens are fake (implement real JWT in production)
- CORS is open to all origins (restrict in production)