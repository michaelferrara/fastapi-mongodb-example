"""Schemas"""

import pydantic


class CreateUserRequest(pydantic.BaseModel):
    name: str


class UpdateUserRequest(pydantic.BaseModel):
    name: str
