FROM python:3-alpine

ENV PYTHONUNBUFFERED=1

ADD entrypoint.py /

ENTRYPOINT ["/entrypoint.py"]
CMD []
