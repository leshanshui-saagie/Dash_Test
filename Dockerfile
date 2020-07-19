FROM python:3.7

USER root

WORKDIR /

COPY . /

RUN pip install -r requirements.txt

EXPOSE 8051

CMD gunicorn -b 0.0.0.0:8051 vis:server
