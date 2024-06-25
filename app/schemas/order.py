from datetime import datetime
from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    item_id: int
    user_id: int
    created_at: datetime

    model_config: ConfigDict = ConfigDict(from_attributes=True)


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    item_id: int | None = None
    user_id: int | None = None
    created_at: datetime | None = None


class OrderResponse(OrderBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
