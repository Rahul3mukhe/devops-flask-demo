FROM python:3.11-slim

WORKDIR /app

# system deps for SQLite and pip
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy application
COPY app /app

ENV FLASK_ENV=production
ENV APP_VERSION=1.0.0

EXPOSE 5000

# Gunicorn entry - app:app refers to app/app.py -> variable app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2"]
