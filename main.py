from fastapi import FastAPI, APIRouter
from views import user_router, assets_router

app = FastAPI()
router = APIRouter()

@router.get("/")
def first():
    return {"message": "Hello World"}

app.include_router(prefix='/first', router=router)
app.include_router(user_router)
app.include_router(assets_router)
