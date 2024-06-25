from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.schemas.order import OrderCreate, OrderResponse, OrderUpdate
from app.db.sql_ins import get_sql
from app.crud import order as crud_order

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/")
def read_orders(
    sql: Session = Depends(get_sql),
):
    return crud_order.get_orders(sql=sql)


@router.post("/")
def create_order(
    order: OrderCreate,
    sql: Session = Depends(get_sql),
) -> OrderResponse:
    return crud_order.create_order(order=order, sql=sql)
