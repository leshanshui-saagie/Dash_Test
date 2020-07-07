FROM python:3.7

USER root

WORKDIR /

COPY . /

RUN pip install -r requirements.txt

EXPOSE 8077

CMD gunicorn -b 0.0.0.0:8077 app:server
