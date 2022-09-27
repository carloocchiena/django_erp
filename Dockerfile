FROM python:3.9-slim

ARG DEBIAN_FRONTEND=noninteractive


RUN apt update \
    && apt install -y --no-install-recommends \
        build-essential \
        graphviz-dev \
    && rm -rf /var/lib/apt/lists/*


COPY . /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r /app/erp/requirements.txt

ENTRYPOINT /app/entrypoint.sh
