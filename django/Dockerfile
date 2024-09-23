# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app


COPY . .



RUN apt-get update \
    && apt-get install -y \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*
    



RUN pip install -r requirements.txt



COPY pro /app


