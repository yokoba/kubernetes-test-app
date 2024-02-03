FROM python:3.12.1-slim-bullseye

WORKDIR /app

RUN mkdir /flask
COPY app.py requirements.txt /flask/

RUN python -m pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r /flask/requirements.txt

EXPOSE 5000
WORKDIR /flask

ENTRYPOINT ["python", "app.py"]
