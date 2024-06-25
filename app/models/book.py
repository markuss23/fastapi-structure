from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.sql_ins import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(length=255), nullable=False)
    authors = relationship("BookAuthor", back_populates="book")
