#!/bin/bash

# Install dependencies
pip install -r src/requirements.txt

# Initialize the vector database
python src/utils.py --init_db

echo "Setup complete."

