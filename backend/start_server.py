#!/usr/bin/env python3
"""
STEM ARENA Backend Server Startup Script
Run this script to start the backend server on port 8000
"""

import uvicorn
from main import app

if __name__ == "__main__":
    print("🚀 Starting STEM ARENA Backend Server...")
    print("📡 Server will be available at: http://127.0.0.1:8000")
    print("📖 API Documentation: http://127.0.0.1:8000/docs")
    print("🔧 Interactive API: http://127.0.0.1:8000/redoc")
    print("\n⚡ Press Ctrl+C to stop the server\n")
    
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=8000, 
        reload=True,
        log_level="info"
    )