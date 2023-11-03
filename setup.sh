#!/bin/bash

# Activate virtual environment or create one if it 
#   does not yet exist
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Creating python virtual environment called 'venv'"
    python -m venv venv
fi

echo "Installing project dependencies..."
pip install -r requirements.txt

