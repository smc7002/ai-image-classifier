# Dockerfile

# Use a minimal Python base image
FROM python:3.11-slim

# Install necessary system packages and clean up afterward
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency list first to use Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY backend backend

# Set environment variable and expose port
ENV PORT=5000
EXPOSE $PORT

# Run the Flask app using Gunicorn
CMD ["gunicorn", "backend.app:app", "--bind", "0.0.0.0:5000"]
