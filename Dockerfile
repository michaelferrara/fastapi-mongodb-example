FROM python:3.11

WORKDIR /code

RUN pip install poetry && touch README.md

COPY ./pyproject.toml /code/pyproject.toml

RUN poetry install

COPY ./fastapi_mongodb_example /code/fastapi_mongodb_example

CMD ["poetry", "run", "uvicorn", "fastapi_mongodb_example.main:app", "--host", "0.0.0.0", "--port", "8080"]
