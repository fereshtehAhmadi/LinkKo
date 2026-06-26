from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./app.db"
    DB_HOST: str = "_"
    DB_PORT: int = 3306
    DB_NAME: str = "_"
    DB_PASS: str = "_"

    APP_NAME: str = "LinkKo"
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8000
    RELOAD: bool = False
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
