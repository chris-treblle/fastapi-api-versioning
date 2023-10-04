from pydantic import BaseModel


class HelloOutputModel(BaseModel):
    greeting: str
