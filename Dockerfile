# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Create app directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . /app/

# Setup Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx and Gunicorn
CMD service nginx start && \
    gunicorn product_management.wsgi:application --bind 0.0.0.0:8000 --workers 3
