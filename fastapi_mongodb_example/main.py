"""Main FastAPI MongoDB Example App"""

from fastapi import FastAPI
from fastapi_mongodb_example.endpoints import user


def create_app() -> FastAPI:
    """App Creator"""
    new_app = FastAPI()

    # Set up routers
    new_app.include_router(user.router, prefix="/user")

    return new_app


app = create_app()
