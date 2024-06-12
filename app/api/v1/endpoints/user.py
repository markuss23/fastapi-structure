from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.db.sql_ins import get_sql
from app.crud import user as crud_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def read_users():
    return {"message": "Hello World"}


@router.post("/")
def create_user(
    user: UserCreate,
    sql: Session = Depends(get_sql),
) -> UserResponse:
    return crud_user.create_user(user=user, sql=sql)
