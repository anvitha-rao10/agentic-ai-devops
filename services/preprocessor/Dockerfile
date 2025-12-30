# Use lightweight Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (if needed later)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file first (for Docker cache)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ app/

# Expose nothing (this is a worker-style service)
# EXPOSE 8000 (only if you later add FastAPI)

# Run the preprocessor
CMD ["python", "-m", "app.main"]
