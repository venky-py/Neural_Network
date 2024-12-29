FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code and requirements.txt
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
