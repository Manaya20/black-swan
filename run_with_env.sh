#!/bin/bash

# Script to run Python commands with properly isolated environment
# Usage: ./run_with_env.sh <python_file_or_command>

cd "$(dirname "$0")"

# Ensure fresh-env exists
if [ ! -d "fresh-env" ]; then
    echo "Creating fresh virtual environment..."
    python3 -m venv --clear fresh-env
    PYTHONNOUSERSITE=1 PYTHONPATH= fresh-env/bin/pip install -r requirements.txt
fi

# Run the command with isolated environment
PYTHONNOUSERSITE=1 PYTHONPATH="$(pwd)" fresh-env/bin/python "$@"
