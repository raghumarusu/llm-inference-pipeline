FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl

# Set working directory
WORKDIR /app

# Copy requirements
COPY src/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY src/ .

# Expose the API port
EXPOSE 8000

# Run the API server
CMD ["uvicorn", "inferencing.inference_api:app", "--host", "0.0.0.0", "--port", "8000"]

