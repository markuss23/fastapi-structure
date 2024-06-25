from app.models.order import Order
from app.schemas.order import OrderCreate, OrderResponse

from sqlalchemy.orm import Session


def get_orders(sql: Session):
    return sql.query(Order).all()


def create_order(order: OrderCreate, sql: Session) -> OrderResponse:
    sql.add(Order(**order.model_dump()))
    sql.commit()
    return (
        sql.query(Order)
        .filter(Order.item_id == order.item_id and Order.user_id == order.user_id)
        .first()
    )
