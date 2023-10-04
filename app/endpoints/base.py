from fastapi import APIRouter
from datetime import datetime
from app.utils.main import get_model_version

router = APIRouter()


@router.get("/ping", response_model=get_model_version('v1', 'TimestampReturnModel'))
async def say_hello():
    return {"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
