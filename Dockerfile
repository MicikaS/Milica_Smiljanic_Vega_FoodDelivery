# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
