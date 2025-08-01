#!/bin/bash

echo "🚀 Starting STEM ARENA Platform..."
echo "======================================"

# Function to handle cleanup on script exit
cleanup() {
    echo ""
    echo "🛑 Shutting down STEM ARENA Platform..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set up signal handlers for cleanup
trap cleanup SIGINT SIGTERM

# Start Backend Server
echo "📡 Starting Backend Server on http://127.0.0.1:8000..."
cd backend
export PATH=$PATH:/home/ubuntu/.local/bin
nohup uvicorn main:app --host 127.0.0.1 --port 8000 --reload > backend.log 2>&1 &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Test backend
echo "🔍 Testing backend connection..."
if curl -s http://127.0.0.1:8000/ > /dev/null; then
    echo "✅ Backend server is running successfully!"
else
    echo "❌ Backend server failed to start!"
    exit 1
fi

# Start Frontend Server (using Python's built-in server)
echo "🌐 Starting Frontend Server on http://127.0.0.1:3000..."
nohup python3 -m http.server 3000 > frontend.log 2>&1 &
FRONTEND_PID=$!

# Wait for frontend to start
sleep 2

echo ""
echo "🎉 STEM ARENA Platform is now running!"
echo "======================================"
echo "📖 Frontend: http://127.0.0.1:3000"
echo "📡 Backend:  http://127.0.0.1:8000"
echo "📋 API Docs: http://127.0.0.1:8000/docs"
echo ""
echo "🔑 Test Login Credentials:"
echo "   Username: testuser"
echo "   Password: password123"
echo ""
echo "⚡ Press Ctrl+C to stop both servers"
echo ""

# Wait for user to stop the servers
wait