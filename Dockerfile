# Base image.
FROM python:3.8

# Working directory.
WORKDIR /app

# Copy and install requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY requirements-prophet.txt .
RUN pip install -r requirements-prophet.txt

# Copy app.
COPY api/ ./api/
COPY run.py .

EXPOSE 5000

# Run app.
CMD [ "python", "run.py" ]