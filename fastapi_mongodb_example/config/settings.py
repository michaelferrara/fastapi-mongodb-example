"""Base Environment Variables"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=(".env", ".env.prod"),
        env_nested_delimiter="__",
    )

    # MongoDB Config
    DB_CONNECTION_STRING: str = ""
    DB_NAME: str = "test_database"
    USER_COLLECTION_NAME: str = "users"


app_settings = Settings()
