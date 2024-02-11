"""User Model"""

from pydantic import BaseModel, Field


class User(BaseModel, populate_by_name=True):
    user_id: str = Field(alias="id")
    name: str
