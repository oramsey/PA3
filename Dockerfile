# Use Python 3.9 as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all files
COPY app.py .
COPY requirements.txt .
COPY templates/ /app/templates/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt




# Expose ports (80 for Apache, 5000 for Flask dev server)
EXPOSE 80 

CMD ["gunicorn", "-b", "0.0.0.0:4217", "-w", "4", "app:app"]
