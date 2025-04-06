FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY train_model.py .

RUN python train_model.py

CMD ["python", "app/main.py"]
