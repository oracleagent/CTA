#!/bin/bash

# Update package list and install necessary packages
echo "Installing system packages..."
sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip git

# Clone the repository
echo "Cloning the repository..."
git clone https://github.com/oracleagent/CTA.git
cd CTA

# Create a virtual environment and activate it
echo "Creating and activating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Initialize the database
echo "Initializing the database..."
python -m src.db.models

echo "Setup completed. Remember to configure your environment variables and configuration files."
