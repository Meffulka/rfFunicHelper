FROM python:3.9

WORKDIR /app
COPY . /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app


CMD ["python", "/app/main.py"]