"""CRUD operations for Item model."""

from sqlalchemy.orm import Session

from mysqldb.models.models_item import Item
from mysqldb.schemas.item_schema import ItemCreate, ItemUpdate


def get_item(db: Session, item_id: int) -> Item | None:
    """Get an item by ID."""
    return db.query(Item).filter(Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100) -> list[Item]:
    """Get a list of items."""
    return db.query(Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: ItemCreate) -> Item:
    """Create a new item."""
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: ItemUpdate) -> Item | None:
    """Update an existing item."""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        for key, value in item.model_dump().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int) -> Item | None:
    """Delete an item."""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
