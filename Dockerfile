# Use an official Python runtime as a parent image
FROM python:3.7-slim


# Set the maintainer of the Dockerfile
MAINTAINER Bipul Dawadi

# Set environment variable to ensure that the python output is sent straight to terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Copy the requirements.txt file from your local directory to the Docker image under /requirements.txt
COPY ./requirements.txt /requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip

RUN pip install -r /requirements.txt

# Make a new directory named app in the Docker image and set it as the working directory
RUN mkdir /app
WORKDIR /app


# Copy the app directory from your local directory to the Docker image under /app
COPY ./app/* /app/

# Change to a non-root user
USER user