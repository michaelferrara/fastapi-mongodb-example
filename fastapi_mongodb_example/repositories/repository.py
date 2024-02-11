"""Abstract Repository Class"""

import uuid
from pydantic import BaseModel
from pymongo.database import Database
from pymongo.collection import Collection
from abc import ABC, abstractmethod
from typing import Any, TypeVar, Generic, Type, Optional
from fastapi_mongodb_example.config.settings import app_settings
from fastapi_mongodb_example.config.mongodb import client

T = TypeVar("T", bound=BaseModel)
IdT = TypeVar("IdT", str, int, uuid.UUID)


class Repository(ABC, Generic[T]):
    """Abstract Base Repository class"""

    def __init__(self, collection_name: str):
        self.db: Database[dict[str, Any]] = client[app_settings.DB_NAME]
        self.collection: Collection[dict[str, Any]] = self.db[collection_name]
        super().__init__()

    @abstractmethod
    def model(self) -> Type[T]:
        raise NotImplementedError()

    @property
    def model_id(self) -> str:
        """The Id of the pydantic model"""
        return "id"

    @property
    def collection_id(self) -> str:
        """The Id of the model in the Collection"""
        return "id"

    def get_by_id(self, item_id: IdT) -> Optional[T]:
        """Get item by id

        Args:
            id: The id of the item to search.

        Returns: The item in the collection with the corresponding id. Returns None if not found
        """
        item = self.collection.find_one({self.model_id: item_id})

        if item is None:
            return None

        return self.model()(**item)

    def create(self, model: T, by_alias: bool = True) -> bool:
        """Create item

        Args:
            model: The model to create

        Returns: True if created and false if not
        """
        res = self.collection.insert_one(model.model_dump(by_alias=by_alias))

        return res.acknowledged

    def update(self, item_id: IdT, model: T, by_alias: bool = True) -> bool:
        """Update item

        Args:
            model: The model to update

        Returns: True if created and false if not
        """
        res = self.collection.update_one({self.collection_id: item_id}, {"$set": model.model_dump(by_alias=by_alias)})

        return res.acknowledged
