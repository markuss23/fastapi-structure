from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.db.sql_ins import get_sql
from app.crud import item as crud_item

from app.schemas.book import BookSchema

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def read_items(
    sql: Session = Depends(get_sql),
):
    return crud_item.get_items(sql=sql)


@router.get(
    "/orders",
)
def read_orders(
    sql: Session = Depends(get_sql),
):
    return crud_item.get_orders(sql=sql)


@router.post("/")
def create_item(
    item: ItemCreate,
    sql: Session = Depends(get_sql),
) -> ItemResponse:
    return crud_item.create_item(item=item, sql=sql)


@router.put("/{item_id}")
def update_item(
    item_id: int,
    item: ItemUpdate,
    sql: Session = Depends(get_sql),
) -> ItemResponse:
    return crud_item.update_item(item_id=item_id, item=item, sql=sql)
