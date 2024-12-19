# Base Image
FROM python:3.13-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# Install PostgreSQL client using apk
RUN apk add --no-cache postgresql-client

# Install dependencies (placeholder)
RUN pip install --no-cache-dir django psycopg2-binary

# Copy project files
COPY . /code/