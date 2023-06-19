# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in the container
WORKDIR /myproject

# Copy the requirements file into the container
COPY ./requirements.txt /myproject/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /myproject
COPY . /myproject/
