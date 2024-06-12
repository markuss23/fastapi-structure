from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserResponse


from sqlalchemy.orm import Session


def create_user(user: UserCreate, sql: Session) -> UserResponse:
    sql.add(User(**user.model_dump()))
    sql.commit()
    sql.refresh(user)
    return user
