FROM python:3.7

USER root

WORKDIR /

COPY . /

RUN pip install -r requirements.txt

EXPOSE 8077

CMD ["python", "app.py"]
