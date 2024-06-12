# Use an official Python image as a base
FROM python:3.9

# Set the working directory to /app
WORKDIR /code

# Copy the requirements file
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/
requirements.txt

# Copy the application code
COPY . .

# Run the command to start the development server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]