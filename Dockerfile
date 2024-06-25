FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Run collectstatic
RUN python manage.py collectstatic --noinput

# Copy project files
COPY . .

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "SD.wsgi:application"]
