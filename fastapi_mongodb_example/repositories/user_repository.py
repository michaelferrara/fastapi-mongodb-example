"""User Repository"""

from typing import Type
from fastapi_mongodb_example.config.settings import app_settings
from fastapi_mongodb_example.models.user import User
from fastapi_mongodb_example.repositories.repository import Repository


class UserRepository(Repository[User]):

    def __init__(self) -> None:
        super().__init__(app_settings.USER_COLLECTION_NAME)

    def model(self) -> Type[User]:
        return User
