from fastapi import APIRouter
from app.v1.endpoints import hello
from app.endpoints import base

router = APIRouter()

router.include_router(hello.router, tags=["v1"])
router.include_router(base.router, tags=["v1"])