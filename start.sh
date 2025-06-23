#!/bin/bash

# Simple start script for Copper Parser Demo
# Just run: ./start.sh then go to http://localhost:3000

set -e

echo "🚀 Starting Copper Parser Demo..."

# Kill any existing processes first
echo "🛑 Stopping any existing servers..."
pkill -f "npm run dev" 2>/dev/null || true
pkill -f "server-manual.py" 2>/dev/null || true
pkill -f "vite" 2>/dev/null || true
sleep 1

# Quick checks
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is required but not installed"
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed"
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm is required but not installed"
    exit 1
fi

# Install webapp deps if needed
if [ ! -d "webapp/node_modules" ]; then
    echo "📦 Installing webapp dependencies..."
    cd webapp
    npm install
    cd ..
fi

# Check if Python API dependencies are installed
if [ ! -f "api/requirements.txt" ]; then
    echo "❌ API requirements.txt not found"
    exit 1
fi

# Check if ports are still in use
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "⚠️  Port 8000 still in use, killing processes..."
    lsof -ti:8000 | xargs kill -9 2>/dev/null || true
    sleep 1
fi

if lsof -Pi :3000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "⚠️  Port 3000 still in use, killing processes..."
    lsof -ti:3000 | xargs kill -9 2>/dev/null || true
    sleep 1
fi

# Start API server in background
echo "🔥 Starting API server on port 8000..."
cd api
python3 server-manual.py &
API_PID=$!
cd ..

# Give API server time to start
sleep 2

# Start webapp in background
echo "🌐 Starting webapp on port 3000..."
cd webapp
npm run dev &
WEBAPP_PID=$!
cd ..

# Give webapp time to start
sleep 3

echo ""
echo "✅ Copper Parser Demo is ready!"
echo "   🌐 Webapp: http://localhost:3000"
echo "   🔥 API:    http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop both servers"

# Cleanup function
cleanup() {
    echo ""
    echo "🛑 Shutting down servers..."
    
    # Kill specific PIDs first
    if [ ! -z "$API_PID" ]; then
        kill $API_PID 2>/dev/null || true
    fi
    if [ ! -z "$WEBAPP_PID" ]; then
        kill $WEBAPP_PID 2>/dev/null || true
    fi
    
    # Kill any remaining processes
    pkill -f "npm run dev" 2>/dev/null || true
    pkill -f "server-manual.py" 2>/dev/null || true
    pkill -f "vite" 2>/dev/null || true
    
    # Force kill processes on ports if needed
    lsof -ti:8000 | xargs kill -9 2>/dev/null || true
    lsof -ti:3000 | xargs kill -9 2>/dev/null || true
    
    echo "✅ Stopped"
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Wait for background processes
wait
