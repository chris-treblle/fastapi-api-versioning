from pydantic import BaseModel


class TimestampReturnModel(BaseModel):
    timestamp: str
