# Use the official Python image as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code to the working directory
COPY src/ .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the entrypoint command to run the Flask app
CMD ["python", "main.py"]