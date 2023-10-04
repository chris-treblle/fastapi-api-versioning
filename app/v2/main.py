from fastapi import APIRouter
from app.v2.endpoints import hello
from app.endpoints import base


router = APIRouter()

router.include_router(hello.router, tags=["v2"])
router.include_router(base.router, tags=["v2"])