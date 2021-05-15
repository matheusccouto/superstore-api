# Base image.
FROM python:3.7-stretch

# Working directory.
WORKDIR /app

# Copy and install requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY requirements-ml.txt .
RUN pip install -r requirements-ml.txt

# Copy app.
COPY api/ ./api/
COPY model/ ./model/
COPY run.py .

EXPOSE 5000

CMD [ "python", "run.py" ]