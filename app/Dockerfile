# Use an official lightweight Python image
FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Expose port
EXPOSE 5000

# Run with gunicorn for production-like server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2"]
