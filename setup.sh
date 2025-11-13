#!/usr/bin/env bash

set -e

VENV_NAME="env"

if ! command -v python3.13 >/dev/null 2>&1; then
    echo "Python 3.13 not found. Please install it first."
    exit 1
fi

echo "Creating virtual environment..."
python3.13 -m venv "$VENV_NAME"

if [ -f "$VENV_NAME/bin/activate" ]; then
    echo "Environment created at ./$VENV_NAME"
    echo "Activate it with:"
    echo "  source $VENV_NAME/bin/activate"
else
    echo "Failed to create virtual environment."
    exit 1
fi

echo "Installing dependencies..."
source "$VENV_NAME/bin/activate"
pip install -r requirements.txt

echo "You are ready to go! :)"