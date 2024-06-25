from fastapi import APIRouter

from app.api.v1.endpoints import user
from app.api.v1.endpoints import item
from app.api.v1.endpoints import order

router = APIRouter(prefix="/v1")

router.include_router(user.router)
router.include_router(item.router)
router.include_router(order.router)
