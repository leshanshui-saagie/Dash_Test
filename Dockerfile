FROM python:3.6

WORKDIR /heads

COPY vis.py /heads/

RUN pip install numpy
RUN pip install dash==1.13.3
RUN pip install gunicorn

EXPOSE 8060

CMD ["gunicorn", "vis:server", "-b", "0.0.0.0:8060"]
