from fastapi import APIRouter
from app.utils.main import get_model_version

router = APIRouter()


@router.get("/hello", response_model=get_model_version('v2', 'HelloOutputModel'))
async def say_hello():
    return {"greeting": "Hello"}


@router.post("/hello/", response_model=get_model_version('v2', 'HelloOutputModel'))
async def say_hello_to_user(input_data: get_model_version('v2', 'HelloInputModel')):
    return {"greeting": f"Hello, {input_data.user}!"}
