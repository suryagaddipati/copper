#!/bin/bash

# Simple start script for Copper Parser Demo
# Runs without installing Python dependencies (FastAPI not available, but parser works)

set -e

echo "🔧 Setting up Copper Parser Demo (Simple Mode)..."

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
cd api
python3 -c "
from copper_parser import validate_copper_syntax
result = validate_copper_syntax('model: test { dimension: id { type: string } }')
print('✅ Parser works!' if result['valid'] else '❌ Parser failed!')
"
cd ..

# Install webapp dependencies
echo "📦 Installing webapp dependencies..."
cd webapp
npm install
cd ..

echo "✅ Setup complete!"
echo ""
echo "⚠️  Note: API server requires FastAPI (pip install fastapi uvicorn)"
echo "   For now, you can:"
echo "   1. Test the parser directly with Python"
echo "   2. Run the webapp (will show connection errors until API is available)"
echo ""

# Show parser test
echo "🧪 Testing parser with example file..."
python3 -c "
import sys
sys.path.append('./api')
from copper_parser import validate_copper_syntax

with open('./examples/ecommerce_orders.copper', 'r') as f:
    content = f.read()

result = validate_copper_syntax(content)
print(f'Example file parse result:')
print(f'  Valid: {result[\"valid\"]}')
print(f'  Models: {result[\"statistics\"][\"total_models\"]}')
print(f'  Dimensions: {result[\"statistics\"][\"total_dimensions\"]}')
print(f'  Measures: {result[\"statistics\"][\"total_measures\"]}')
"

echo ""
echo "🌐 Starting webapp on http://localhost:3000"
echo "   (Note: API features will not work without FastAPI installed)"
cd webapp
npm run dev