"""User Service"""

from typing import Optional
from fastapi_mongodb_example.models.user import User
from fastapi_mongodb_example.repositories.user_repository import UserRepository


class UserService:
    """User Service"""

    def get_user(self, user_id: str) -> Optional[User]:
        user_repository = UserRepository()

        return user_repository.get_by_id(user_id)

    def create_user(self, user: User) -> bool:
        """Creates a User"""
        user_repository = UserRepository()

        return user_repository.create(user)

    def update_user(self, user_id: str, user: User) -> bool:
        """Creates a User"""
        user_repository = UserRepository()

        return user_repository.update(user_id, user)
