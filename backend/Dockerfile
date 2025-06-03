# backend/Dockerfile

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
ENV PORT=10000
EXPOSE $PORT

# Run the app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
