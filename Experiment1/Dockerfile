# Author: Akarsh Seggemu
# Created: 2025-01-24
#
# Use an official Python image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# execute the command
CMD ["python", "app.py"]
