from pydantic import BaseModel


class HelloInputModel(BaseModel):
    name: str
