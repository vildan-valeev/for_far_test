FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock /

RUN pip3 install poetry

RUN poetry install