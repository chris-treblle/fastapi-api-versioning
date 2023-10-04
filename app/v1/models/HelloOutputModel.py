from pydantic import BaseModel


class HelloOutputModel(BaseModel):
    message: str
