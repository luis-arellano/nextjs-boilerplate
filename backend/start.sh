#!/bin/bash

echo "🚀 Setting up Flask backend..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements if they're not already installed
echo "📋 Checking dependencies..."
pip install -q -r requirements.txt

echo "🚀 Starting Flask server..."
echo "📍 Server: http://localhost:5001"
echo "🔗 CORS enabled for: http://localhost:3000"
echo "Press Ctrl+C to stop"
echo

python app.py