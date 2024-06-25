from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    title: str
    description: str

    model_config: ConfigDict = ConfigDict(from_attributes=True)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class ItemResponse(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
