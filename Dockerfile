FROM python:3.10-slim

WORKDIR /app

COPY app/ app/
COPY requirements.txt .
COPY app/sentiment_model.pkl app/


RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "app/main.py"]
