from pydantic import BaseModel


class UserCreateInput(BaseModel):
    name: str


class UserFavoriteAddInput(BaseModel):
    user_id: int
    symbol: str


class StandardOutputInput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str
