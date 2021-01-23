FROM python:3.9.1-buster

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
      build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV APP_ROOT /app
WORKDIR $APP_ROOT

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile $APP_ROOT
COPY Pipfile.lock $APP_ROOT

RUN pipenv sync

ADD . /app

