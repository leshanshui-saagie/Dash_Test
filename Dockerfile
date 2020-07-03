FROM python:3.7

ENV DASH_DEBUG_MODE True

RUN set -ex && pip install -r requirements.txt

USER root
RUN apt-get update && apt-get install -y --no-install-recommends curl

COPY app /

WORKDIR /

EXPOSE 8050
CMD ["gunicorn", "-b", "0.0.0.0:8050", "app"]