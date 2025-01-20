# Use an official Python runtime as a base image
FROM python:3.12-slim

# Install dependencies for interacting with PostgreSQL and the API
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the web service will run on (optional)
EXPOSE 8000

# Run the application
CMD ["python3", "main.py"]
