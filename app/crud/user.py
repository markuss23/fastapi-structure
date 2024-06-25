from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserResponse


from sqlalchemy.orm import Session


def get_users(sql: Session):
    return sql.query(User).all()


def create_user(user: UserCreate, sql: Session) -> UserResponse:
    sql.add(User(**user.model_dump()))
    sql.commit()
    return (
        sql.query(User)
        .filter(User.email == user.email and User.name == user.name)
        .first()
    )
