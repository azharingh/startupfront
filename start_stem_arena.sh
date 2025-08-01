#!/bin/bash

# STEM ARENA - Startup Script
# This script starts both the backend API server and serves the frontend

echo "🚀 Starting STEM ARENA..."
echo "================================"

# Function to handle cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down STEM ARENA..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set up trap to handle Ctrl+C
trap cleanup SIGINT SIGTERM

# Start Backend Server
echo "📡 Starting Backend Server..."
cd backend
python3 main.py &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 3

# Check if backend started successfully
if ! ps -p $BACKEND_PID > /dev/null; then
    echo "❌ Failed to start backend server"
    exit 1
fi

echo "✅ Backend server started (PID: $BACKEND_PID)"
echo "   📖 API Documentation: http://127.0.0.1:8000/docs"
echo "   🔧 Interactive API: http://127.0.0.1:8000/redoc"

# Start Frontend Server (using Python's built-in HTTP server)
echo ""
echo "🌐 Starting Frontend Server..."
python3 -m http.server 3000 &
FRONTEND_PID=$!

# Wait a moment for frontend to start
sleep 2

# Check if frontend started successfully
if ! ps -p $FRONTEND_PID > /dev/null; then
    echo "❌ Failed to start frontend server"
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

echo "✅ Frontend server started (PID: $FRONTEND_PID)"
echo "   🎮 Main App: http://127.0.0.1:3000/pj.html"
echo "   🔢 Competition: http://127.0.0.1:3000/competition.html"

echo ""
echo "🎉 STEM ARENA is now running!"
echo "================================"
echo "Backend API: http://127.0.0.1:8000"
echo "Frontend: http://127.0.0.1:3000"
echo ""
echo "Test credentials:"
echo "  Username: testuser"
echo "  Password: password123"
echo ""
echo "Press Ctrl+C to stop all servers"
echo "================================"

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID