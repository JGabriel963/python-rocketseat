from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=["Usuários"], prefix="/users")

@users_routes.post("/")
async def criar_usuario():
    return JSONResponse(
        content={"message": "User created"},
        status_code=201
    )
