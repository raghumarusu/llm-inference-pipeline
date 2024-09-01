#!/bin/bash

# Build Docker image
docker build -t llm-inference-pipeline:latest .

# Run Docker container
docker run -d -p 8000:8000 llm-inference-pipeline:latest

echo "Deployment complete."

