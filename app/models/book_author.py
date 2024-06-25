from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.sql_ins import Base
from sqlalchemy.ext.associationproxy import association_proxy


class BookAuthor(Base):
    __tablename__ = "book_authors"
    book_id = Column(ForeignKey("books.id"), primary_key=True)
    author_id = Column(ForeignKey("authors.id"), primary_key=True)
    blurb = Column(String(length=255), nullable=False)
    book = relationship("Book", back_populates="authors")
    author = relationship("Author", back_populates="books")

    # proxies
    author_name = association_proxy(target_collection="author", attr="name")
    book_title = association_proxy(target_collection="book", attr="title")
