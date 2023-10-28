FROM python:3.11.2-slim-buster

WORKDIR /opt/app

COPY src.python.microservices/microservices.pex /opt/app/microservices.pex

ENTRYPOINT ["/bin/bash", "-c", "/opt/app/microservices.pex"]
