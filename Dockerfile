# Base image.
FROM python:3.8-slim

# Working directory.
WORKDIR /app

# Copy and install requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app.
COPY api/ ./api/
COPY run.py .

# Run app.
CMD [ "python", "run.py" ]