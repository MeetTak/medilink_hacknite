#!/bin/bash

# Activate conda environment and run AI server
echo "🔧 Activating conda environment..."

# Initialize conda in bash shell
eval "$(conda shell.bash hook)"

# Activate the medilink environment
conda activate medilink

# Run the AI server
echo "🚀 Starting AI server in medilink environment..."
python ai_server.py
