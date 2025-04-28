# Use an official Python runtime as the base image
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8765

CMD ["python", "-u", "server.py"]