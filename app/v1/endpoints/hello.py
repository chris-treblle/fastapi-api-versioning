from fastapi import APIRouter
from app.utils.main import get_model_version

router = APIRouter()


@router.get("/hello", response_model=get_model_version('v1', 'HelloOutputModel'))
async def say_hello():
    return {"message": "Hello"}


@router.post("/hello", response_model=get_model_version('v1', 'HelloOutputModel'))
async def say_hello_to_name(input_data: get_model_version('v1', 'HelloInputModel')):
    return {"message": f"Hello, {input_data.name}!"}
