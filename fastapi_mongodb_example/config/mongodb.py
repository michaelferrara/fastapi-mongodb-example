"""MongoDB Client Config"""

from typing import Any
from pymongo import MongoClient
from fastapi_mongodb_example.config.settings import app_settings

client: MongoClient[dict[str, Any]] = MongoClient(app_settings.DB_CONNECTION_STRING)
