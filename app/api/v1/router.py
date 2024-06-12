from fastapi import APIRouter

from app.api.v1.endpoints import user

router = APIRouter(prefix="/v1")

router.include_router(user.router)
