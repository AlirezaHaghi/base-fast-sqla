from fastapi import FastAPI
from contextlib import asynccontextmanager
from .authentication import router as authentication_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    from .db import init_db
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(authentication_router, tags=["auth"])

@app.get("/health-check")
async def health():
    return {"message": "healthy"}

