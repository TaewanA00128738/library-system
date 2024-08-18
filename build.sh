#!/bin/bash

# Define variables
ENV_DIR="myenv"
SCRIPT="main.py"
DIST_DIR="dist"
EXECUTABLE="library_system"

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv $ENV_DIR

# Activate the virtual environment
source $ENV_DIR/bin/activate

# Install required packages
echo "Installing required packages..."
pip install pyinstaller

# Run tests
echo "Running tests..."
python -m unittest test-library-system.py
if [ $? -ne 0 ]; then
    echo "Tests failed. Exiting."
    deactivate
    exit 1
fi

# Create the executable
echo "Creating executable..."
pyinstaller --onefile $SCRIPT

# Check if the executable was created successfully
if [ -f "$DIST_DIR/$EXECUTABLE" ]; then
    echo "Executable created successfully."
else
    echo "Failed to create executable. Exiting."
    deactivate
    exit 1
fi

# Deactivate the virtual environment
deactivate

echo "Build process completed successfully."