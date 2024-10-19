# Use an official Python runtime as a parent image
FROM python:3.12-slim

# install necessary dependencies
RUN apt-get update \
    && apt-get install -y \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    netcat-traditional


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port on which the app will run
EXPOSE 8000

RUN ["chmod", "+x", "/app/entrypoint.sh"]

ENTRYPOINT ["./entrypoint.sh"]