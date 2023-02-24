from pydantic import BaseModel
from typing import List

class UserCreateInput(BaseModel):
    name: str


class UserFavoriteAddInput(BaseModel):
    user_id: int
    symbol: str


class StandardOutputInput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str


class Favorite(BaseModel):
    id: int
    symbol: str
    use_id: int


    class Config:
        orm_mode = True

class ListUserOutput(BaseModel):
    id: int
    name: str
    favorites: List[Favorite]


    class Config:
        orm_mode = True
