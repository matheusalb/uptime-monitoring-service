"""Config module for database settings."""

from functools import lru_cache

from pydantic import Field, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for database connection."""

    PROJECT_NAME: str = "MySQL Database"
    API_V1_STR: str = "/api"

    DB_USER: str = Field(default="root")
    DB_PASSWORD: str = Field(default="password")
    DB_HOST: str = Field(default="localhost")
    DB_PORT: int = Field(default=3306)
    DB_NAME: str = Field(default="mydatabase")

    DATABASE_URL: str = Field(default="")

    # @classmethod
    @field_validator("DATABASE_URL", mode="before")
    def assemble_db_connection(cls, value: str, info: ValidationInfo) -> str:  # noqa: N805
        """Assemble the database connection URL."""
        if isinstance(value, str) and value:
            return value
        data = info.data
        return (
            f"mysql+pymysql://{data.get('DB_USER')}:{data.get('DB_PASSWORD')}"
            f"@{data.get('DB_HOST')}:{data.get('DB_PORT')}/{data.get('DB_NAME')}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )

@lru_cache
def get_settings() -> Settings:
    """Get settings from environment variables."""
    return Settings()
