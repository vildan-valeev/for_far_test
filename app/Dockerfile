FROM python:3.8

RUN apt-get update \
    && apt-get install -y \
    wkhtmltopdf
#RUN apt install wkhtmltopdf

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock /



RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
