FROM python:3.7

ENV DASH_DEBUG_MODE False

COPY app.py /
COPY requirements.txt /

USER root
RUN apt-get update && apt-get install -y --no-install-recommends curl
RUN pip install -r requirements.txt

WORKDIR /

EXPOSE 8078
CMD ["python", "app.py"]
