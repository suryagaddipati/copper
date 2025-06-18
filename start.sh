#!/bin/bash

# Start script for Copper Parser Demo
# Runs both API backend and webapp frontend

set -e

echo "🔧 Setting up Copper Parser Demo..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is required but not installed"
    exit 1
fi

# Check if Node.js is available
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed"
    exit 1
fi

# Install API dependencies
echo "📦 Installing API dependencies..."
cd api
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Install webapp dependencies
echo "📦 Installing webapp dependencies..."
cd webapp
npm install
cd ..

echo "✅ Setup complete!"
echo ""
echo "🚀 Starting services..."

# Start API in background
echo "🔥 Starting API server on http://localhost:8000"
cd api
source venv/bin/activate
python main.py &
API_PID=$!
cd ..

# Wait a moment for API to start
sleep 2

# Start webapp in background
echo "🌐 Starting webapp on http://localhost:3000"
cd webapp
npm run dev &
WEBAPP_PID=$!
cd ..

echo ""
echo "✅ Both services are running!"
echo "   📡 API: http://localhost:8000"
echo "   🌐 Webapp: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop both services"

# Function to cleanup processes
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    kill $API_PID 2>/dev/null || true
    kill $WEBAPP_PID 2>/dev/null || true
    echo "✅ Services stopped"
    exit 0
}

# Trap Ctrl+C
trap cleanup SIGINT

# Wait for both processes
wait $API_PID $WEBAPP_PID