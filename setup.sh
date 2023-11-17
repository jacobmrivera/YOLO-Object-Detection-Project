#!/bin/bash

# Activate virtual environment or create one if it 
#   does not yet exist
if [ -d "venv" ]; then
    source venv/Scripts/activate
else
    echo "Creating python virtual environment called 'venv'"
    python -m venv venv
    source venv/Scripts/activate 
fi

echo "Installing project dependencies..."
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
echo "Dependencies installed."

