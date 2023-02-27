from fastapi import FastAPI, APIRouter
from views import user_router, assets_router

app = FastAPI()
router = APIRouter()


app.include_router(user_router)
app.include_router(assets_router)

