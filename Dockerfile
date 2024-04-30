# Use the specified Python image
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any dependencies
RUN pip3 install --user -r requirements.txt

# Copy the rest of your application's code
COPY . /app

# Specify the command to run on container start
CMD ["python3", "app.py"]
