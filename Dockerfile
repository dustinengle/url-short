FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .
COPY src/app.py .

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python app.py
