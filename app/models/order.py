from typing import Any

# models/order.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared
from app.db.sql_ins import Base


class Order(Base):
    __tablename__: str = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))

    user: _RelationshipDeclared[Any] = relationship("User", back_populates="orders")
    item: _RelationshipDeclared[Any] = relationship("Item", back_populates="orders")
