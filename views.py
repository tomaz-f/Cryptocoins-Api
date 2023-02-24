from typing import List
from fastapi import APIRouter, HTTPException
from services import UserService, FavoriteService
from schemas import (
    UserCreateInput, StandardOutputInput, ErrorOutput,
    UserFavoriteAddInput, UserListOutput
)

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')


@user_router.post('/create', response_model=StandardOutputInput,
                  responses={400: {'model': ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandardOutputInput(message='User created')
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@user_router.delete('/delete/{user.id}', response_model=StandardOutputInput)
async def user_delete(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return StandardOutputInput(message='User deleted')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.post('/favorite/add', response_model=StandardOutputInput,
                  responses={400: {'model': ErrorOutput}})
async def user_favorite_add(favorite_add: UserFavoriteAddInput):
    try:
        await FavoriteService.add_favorite(
            user_id=favorite_add.user_id, symbol=favorite_add.symbol
        )
        return StandardOutputInput(message='Favorite added')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete('/favorite/remove/{user_id}', response_model=StandardOutputInput,
                    responses={400: {'model': ErrorOutput}})
async def user_favorite_remove(user_id: int, symbol: str):
    try:
        await FavoriteService.remove_favorite(user_id=user_id, symbol=symbol)
        return StandardOutputInput(message='Favorite removed')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.get('/list', response_model=List[UserListOutput], 
                 responses={400: {'model': ErrorOutput}})
async def user_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(400, detail=str(error))