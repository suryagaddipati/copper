#!/bin/bash

# Start script for Copper Parser Demo using manual HTTP server
# Works without FastAPI - uses built-in Python HTTP server

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

# Test the parser first
echo "🧪 Testing Copper parser..."
python3 -c "
import sys
sys.path.append('./api')
from copper_parser import validate_copper_syntax

# Test basic parsing
result = validate_copper_syntax('model: test { dimension: id { type: string } }')
print('✅ Basic parser works!' if result['valid'] else '❌ Basic parser failed!')

# Test with example file
try:
    with open('./examples/ecommerce_orders.copper', 'r') as f:
        content = f.read()
    result = validate_copper_syntax(content)
    print(f'✅ Example file parsed: {result[\"statistics\"][\"total_models\"]} models, {result[\"statistics\"][\"total_dimensions\"]} dimensions')
except Exception as e:
    print(f'❌ Example file test failed: {e}')
"

# Install webapp dependencies
echo "📦 Installing webapp dependencies..."
cd webapp
npm install
cd ..

echo "✅ Setup complete!"
echo ""
echo "🚀 Starting services..."

# Start manual API server in background
echo "🔥 Starting API server on http://localhost:8000"
cd api
python3 server-manual.py &
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