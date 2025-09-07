#!/bin/bash

echo "🧪 Running Flask backend tests..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run tests with verbose output
python -m unittest discover -s tests -v

echo "✅ Tests completed!"