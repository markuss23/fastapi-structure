# models/order.py
import pytz
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.sql_ins import Base
from datetime import datetime
from app.core.config import settings


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(ForeignKey("items.id"))
    user_id = Column(ForeignKey("users.id"))
    created_at = Column(
        DateTime,
        default=datetime.now(tz=pytz.timezone(settings.app.timezone)),
    )
    user = relationship("User", back_populates="items")
    item = relationship("Item", back_populates="users")
