# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /project1

# Copy the current directory contents into the container at /app
COPY . /project1

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for the Django app
EXPOSE 8000

# Define the command to run your application
CMD ["python3", "manage.py", "runserver"]
