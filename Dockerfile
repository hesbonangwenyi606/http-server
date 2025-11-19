# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything to /app in the container
COPY . /app

# Expose port 8080
EXPOSE 8080

# Run the server
CMD ["python3", "http_server.py"]

