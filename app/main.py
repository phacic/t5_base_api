from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api.v1 import v1_router
from app.core.config import settings
from app.internal import default_translator

app = FastAPI(title="t5_base_api")

# routers
app.include_router(router=v1_router, prefix=settings.API_V1, tags=["v1"])


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    """
    redirect to docs
    """
    return RedirectResponse(url="/docs")


@app.on_event("startup")
async def init_models() -> None:
    """
    initialize models on app startup
    """
    default_translator.init_model()
