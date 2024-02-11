"""Example API Routes"""

from typing import Any
import uuid
from fastapi import APIRouter, Depends, Path, exceptions
from fastapi_mongodb_example.models.schemas import CreateUserRequest, UpdateUserRequest
from fastapi_mongodb_example.models.user import User

from fastapi_mongodb_example.services.user_service import UserService

router = APIRouter()


def get_user_service() -> UserService:
    """Get User Service"""
    return UserService()


@router.post("", response_model=User)
def create(
    create_user_request: CreateUserRequest,
    user_service: UserService = Depends(get_user_service),
) -> dict[str, Any]:
    new_user = User(id=str(uuid.uuid4()), name=create_user_request.name)
    user_created = user_service.create_user(new_user)

    if user_created is False:
        raise exceptions.HTTPException(400, f"Failed to create user with name: {create_user_request.name}")

    return new_user.model_dump(by_alias=True)


@router.get("/{id}", response_model=User)
def get_by_id(user_id: str = Path(alias="id"), user_service: UserService = Depends(get_user_service)) -> dict[str, Any]:
    user: User | None = user_service.get_user(user_id)

    if user is None:
        raise exceptions.HTTPException(404, f"Failed to find user with id: {user_id}")

    return user.model_dump(by_alias=True)


@router.put("/{id}", response_model=User)
def update(
    update_user_request: UpdateUserRequest,
    user_id: str = Path(alias="id"),
    user_service: UserService = Depends(get_user_service),
) -> dict[str, Any]:
    user = User(id=user_id, name=update_user_request.name)
    user_updated = user_service.update_user(user_id, user)

    if user_updated is False:
        raise exceptions.HTTPException(400, f"Failed to update user with name: {update_user_request.name}")

    return user.model_dump(by_alias=True)
