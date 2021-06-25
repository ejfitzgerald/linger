FROM python:3-alpine

ADD entrypoint.py /

ENTRYPOINT ["/entrypoint.py"]
CMD []
