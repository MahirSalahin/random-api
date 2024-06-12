# Use an official Python image as a base
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

RUN useradd -m -u 1000 user

USER user

ENV HOME =/home/user \
          PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app
# Copy the application code
COPY --chown=user . $HOME/app

# Run the command to start the development server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]