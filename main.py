"""FastAPI high-performance API - Clean Architecture."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.health import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    yield
    # Cleanup


app = FastAPI(
    title="High-Performance API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

app.include_router(health_router, tags=["health"])


@app.get("/")
async def root():
    return {"message": "API running"}
