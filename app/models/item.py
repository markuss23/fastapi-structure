from typing import Any

# models/item.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared
from app.db.sql_ins import Base


class Item(Base):
    __tablename__: str = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=255), index=True)
    description = Column(String(length=255), index=True)
    orders: _RelationshipDeclared[Any] = relationship("Order", back_populates="item")
