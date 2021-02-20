FROM python:3.9.1-buster

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
      build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV APP_ROOT /app
WORKDIR $APP_ROOT

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml $APP_ROOT
COPY poetry.lock $APP_ROOT

RUN poetry install

ADD . /app
