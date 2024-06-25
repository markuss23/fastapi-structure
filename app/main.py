from fastapi import FastAPI

from app.db.sql_ins import get_sql, engine

from app.models import order, user, item, author, book, book_author

from app.api.v1 import router

order.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
item.Base.metadata.create_all(bind=engine)
author.Base.metadata.create_all(bind=engine)
book.Base.metadata.create_all(bind=engine)
book_author.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.router.include_router(router.router)
