from fastapi import APIRouter

from app.api.v1 import translate

v1_router = APIRouter()
v1_router.include_router(router=translate.router, prefix="/translate")
