#!/bin/bash

# Stop the bot if it's running
echo "Stopping the bot..."
pkill -f main.py

# Pull the latest changes from the repository
echo "Pulling the latest changes..."
git pull origin main

# Install/update dependencies
echo "Installing/updating dependencies..."
source venv/bin/activate
pip install -r requirements.txt

# Run database migrations (if any)
echo "Running database migrations..."
python -m src.db.models

# Start the bot
echo "Starting the bot..."
nohup python -m src.main &

echo "Deployment completed."
