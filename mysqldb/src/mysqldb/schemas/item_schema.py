"""Item schema module for MySQL operations."""

from datetime import datetime

from pydantic import BaseModel


class ItemBase(BaseModel):
    """Base model for item."""

    url: str
    frequency: float

class ItemCreate(ItemBase):
    """Model for creating an item."""


class ItemUpdate(ItemBase):
    """Model for updating an item."""


class ItemInDB(ItemBase):
    """Model for item in the database."""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        """Model for configuration."""

        orm_mode = True

class Item(ItemBase):
    """Model for item."""
