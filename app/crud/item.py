from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse


from app.models.author import Author
from app.models.book import Book
from app.models.order import Order
from sqlalchemy.orm import Session, joinedload


def get_items(sql: Session):
    return sql.query(Item).all()


def get_orders(sql: Session):
    print(
        sql.query(Item).options(joinedload(Item.users).options(joinedload(Order.user)))
    )
    return (
        sql.query(Item)
        .options(joinedload(Item.users).options(joinedload(Order.user)))
        .all()
    )


def create_item(item: ItemCreate, sql: Session) -> ItemResponse:
    sql.add(Item(**item.model_dump()))
    sql.commit()
    return (
        sql.query(Item)
        .filter(Item.title == item.title and Item.description == item.description)
        .first()
    )
