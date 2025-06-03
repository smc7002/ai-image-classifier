# Use official Python slim base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY backend/ backend/

# Expose the port (default 5000)
ENV PORT=5000
EXPOSE $PORT

# Run the app using Gunicorn
CMD ["gunicorn", "backend.app:app", "--bind", "0.0.0.0:5000"]
