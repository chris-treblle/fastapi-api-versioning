from pydantic import BaseModel


class HelloInputModel(BaseModel):
    user: str
