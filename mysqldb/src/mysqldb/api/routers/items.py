"""MySQL Database API for managing items."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

import mysqldb.crud.crud_item as crud
from mysqldb.config.database import get_db
from mysqldb.schemas.item_schema import Item, ItemCreate, ItemUpdate

router = APIRouter(
    prefix="/api/items",
    tags=["items"],
)


@router.get("/")
def read_items(
    db: Annotated[Session, Depends(get_db)],
    skip: Annotated[int, Query(ge=0, description="Number of items to skip")] = 0,
    limit: Annotated[
        int,
        Query(gt=0, description="Maximum number of items to return"),
    ] = 100,
) -> list[Item]:
    """Retrieve a list of items."""
    return [
        Item(url=str(item.url), frequency=float(item.frequency))
        for item in crud.get_items(db, skip=skip, limit=limit)
    ]


@router.get("/{item_id}")
def read_item(
    item_id: int,
    db: Annotated[Session, Depends(get_db)],
) -> Item:
    """Retrieve a single item by ID."""
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return (
        Item(
            url=str(db_item.url),
            frequency=float(db_item.frequency),
        )
        if db_item
        else Item(url="", frequency=0.0)
    )


@router.post("/")
def create_new_item(
    item: ItemCreate,
    db: Annotated[Session, Depends(get_db)],
) -> Item:
    """Create a new item."""
    db_item = crud.create_item(db, item=item)
    return (
        Item(url=str(db_item.url), frequency=float(db_item.frequency))
        if db_item
        else Item(url="", frequency=0.0)
    )


@router.put("/{item_id}")
def update_item(
    item_id: int,
    item: ItemUpdate,
    db: Annotated[Session, Depends(get_db)],
) -> Item:
    """Update an existing item."""
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(url=str(db_item.url), frequency=float(db_item.frequency))


@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    db: Annotated[Session, Depends(get_db)],
) -> Item:
    """Delete an item."""
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(url=str(db_item.url), frequency=float(db_item.frequency))
