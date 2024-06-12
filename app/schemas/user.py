from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    email: str

    model_config: ConfigDict = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None


class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
