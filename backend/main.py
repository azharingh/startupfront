from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
import json
import random
from datetime import datetime

app = FastAPI(title="STEM ARENA Backend", version="1.0.0")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class LoginRequest(BaseModel):
    username: str
    password: str

class SignupRequest(BaseModel):
    username: str
    email: str
    password: str

class SubmissionRequest(BaseModel):
    task_id: str
    solution: str
    user_id: str

# In-memory storage (replace with database in production)
users_db = {
    "testuser": {
        "id": "testuser",
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",  # In production, hash passwords
        "level": 3,
        "rank": "WARRIOR",
        "gems": 1247,
        "total_score": 2500,
        "completed_challenges": 15,
        "accuracy": 85.2
    }
}

competitions_db = {
    "current_task": {
        "id": "task_001",
        "title": "Binary Search Challenge",
        "description": "Implement an efficient binary search algorithm",
        "difficulty": "Medium",
        "time_limit": 30,
        "test_cases": [
            {"input": "[1,2,3,4,5], target=3", "expected": "2"},
            {"input": "[1,3,5,7,9], target=7", "expected": "3"}
        ]
    }
}

@app.get("/")
async def root():
    return {"message": "STEM ARENA Backend API", "status": "active"}

@app.post("/login")
async def login(request: LoginRequest):
    user = users_db.get(request.username)
    if not user or user["password"] != request.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    return {
        "success": True,
        "user": {
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
            "level": user["level"],
            "rank": user["rank"],
            "gems": user["gems"]
        },
        "token": f"fake_jwt_token_{user['id']}"  # In production, use real JWT
    }

@app.post("/signup")
async def signup(request: SignupRequest):
    if request.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    
    # Create new user
    new_user = {
        "id": request.username,
        "username": request.username,
        "email": request.email,
        "password": request.password,  # In production, hash passwords
        "level": 1,
        "rank": "NOVICE",
        "gems": 0,
        "total_score": 0,
        "completed_challenges": 0,
        "accuracy": 0.0
    }
    
    users_db[request.username] = new_user
    
    return {
        "success": True,
        "user": {
            "id": new_user["id"],
            "username": new_user["username"],
            "email": new_user["email"],
            "level": new_user["level"],
            "rank": new_user["rank"],
            "gems": new_user["gems"]
        },
        "token": f"fake_jwt_token_{new_user['id']}"
    }

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return {
        "id": user["id"],
        "username": user["username"],
        "email": user["email"],
        "level": user["level"],
        "rank": user["rank"],
        "gems": user["gems"],
        "total_score": user["total_score"],
        "completed_challenges": user["completed_challenges"],
        "accuracy": user["accuracy"]
    }

@app.get("/competition/task")
async def get_competition_task():
    return competitions_db["current_task"]

@app.post("/competition/submit")
async def submit_solution(request: SubmissionRequest):
    user = users_db.get(request.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Simple solution validation (in production, run actual tests)
    score = random.randint(60, 100)  # Random score for demo
    is_correct = score >= 70
    
    if is_correct:
        # Update user stats
        user["gems"] += 50
        user["total_score"] += score
        user["completed_challenges"] += 1
        
        # Update accuracy
        total_attempts = user["completed_challenges"]
        user["accuracy"] = (user["accuracy"] * (total_attempts - 1) + score) / total_attempts
    
    return {
        "success": True,
        "score": score,
        "is_correct": is_correct,
        "gems_earned": 50 if is_correct else 0,
        "message": "Great job!" if is_correct else "Keep trying!",
        "user_stats": {
            "gems": user["gems"],
            "total_score": user["total_score"],
            "completed_challenges": user["completed_challenges"],
            "accuracy": round(user["accuracy"], 1)
        }
    }

# Additional endpoints for extended functionality
@app.get("/leaderboard")
async def get_leaderboard():
    sorted_users = sorted(
        users_db.values(),
        key=lambda x: x["total_score"],
        reverse=True
    )
    
    return {
        "leaderboard": [
            {
                "rank": idx + 1,
                "username": user["username"],
                "level": user["level"],
                "total_score": user["total_score"],
                "gems": user["gems"]
            }
            for idx, user in enumerate(sorted_users[:10])
        ]
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)