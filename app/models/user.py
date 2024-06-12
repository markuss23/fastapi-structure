from typing import Any

# models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared
from app.db.sql_ins import Base


class User(Base):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), index=True)
    email = Column(String(length=255), unique=True, index=True)
    orders: _RelationshipDeclared[Any] = relationship("Order", back_populates="user")
