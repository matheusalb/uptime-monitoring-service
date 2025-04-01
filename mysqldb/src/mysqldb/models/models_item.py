"""Define Item model."""

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func

from mysqldb.config.database import Base


class Item(Base):
    """Item model for MySQL database."""

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(255), nullable=False)
    frequency = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
