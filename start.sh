#!/bin/bash

# Simple start script for Copper Parser Demo
# Just run: ./start.sh then go to http://localhost:3000

set -e

echo "🚀 Starting Copper Parser Demo..."

# Quick checks
if ! command -v python3 &> /dev/null; then
    echo "❌ Need Python3"
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "❌ Need Node.js"
    exit 1
fi

# Install webapp deps if needed
if [ ! -d "webapp/node_modules" ]; then
    echo "📦 Installing dependencies..."
    cd webapp && npm install && cd ..
fi

# Start API server
echo "🔥 Starting API server..."
cd api && python3 server-manual.py &
API_PID=$!
cd ..

# Start webapp
echo "🌐 Starting webapp..."
cd webapp && npm run dev &
WEBAPP_PID=$!
cd ..

sleep 2
echo ""
echo "✅ Ready! Open: http://localhost:3000"
echo "   (API: http://localhost:8000)"
echo ""
echo "Press Ctrl+C to stop"

# Cleanup on exit
trap 'echo "🛑 Stopping..."; kill $API_PID $WEBAPP_PID 2>/dev/null; exit' SIGINT

# Wait
wait