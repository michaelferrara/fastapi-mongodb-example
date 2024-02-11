# fastapi-mongodb-example

Example FastAPI MongoDB App

# Prerequisites

Python 3.11

### Set up and activate environment

```bash
python -m venv .venv
```

### Install Poetry

```bash
pip install poetry
```

### Install Dependencies
```bash
poetry install
```

# Running the Application

## Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

## Dev

Start environment and intall dependencies then run:

```bash
poetry run uvicorn fastapi_mongodb_example.main:app --reload --port 8080
```

## Environment Variables

DB_CONNECTION_STRING: The MongoDB Connection string

# Development

## Run Unit Tests

```bash
poetry run pytest tests
```

## Run Pylint

Code

```bash
poetry run pylint fastapi_mongodb_example
```

Tests

```bash
poetry run pylint tests
```

## Run Black Formatter

```bash
poetry run black --check .
```

## Run MyPy

```bash
poetry run mypy --strict .
```
