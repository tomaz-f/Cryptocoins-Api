from database.models import User
from database.connection import async_session
from sqlalchemy import delete


class UserService:
    async def create_user(name):
        async with async_session() as session:
            session.add(User(name=name))
            await session.commit()

    async def delete_user(user_id):
        async with async_session() as session:
            await session.execute(delete(User).where(User.id == user_id))
            await session.commit()