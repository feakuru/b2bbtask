FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DEBUG "FALSE"

RUN mkdir /b2bbtask

WORKDIR /b2bbtask

COPY poetry.lock pyproject.toml /b2bbtask/
RUN pip install poetry
RUN poetry install --without dev
COPY . /b2bbtask/
