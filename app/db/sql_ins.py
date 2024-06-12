from typing import Any, Generator

from sqlalchemy.orm.session import Session
from ..core.config import settings
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

timeout = 60000
MARIADB_DATABASE_URL: str = settings.sql.url()

engine: Engine = create_engine(MARIADB_DATABASE_URL, pool_pre_ping=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: Any = declarative_base()


def get_sql() -> Generator[Session, Any, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
