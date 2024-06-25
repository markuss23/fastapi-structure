from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.sql_ins import Base


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255), nullable=False)
    books = relationship("BookAuthor", back_populates="author")
