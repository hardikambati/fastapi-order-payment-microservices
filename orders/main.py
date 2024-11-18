from fastapi import (
    FastAPI
)
from contextlib import asynccontextmanager

from api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from db import (
    engine,
    database,
    metadata,
)


# accept connections from
origins = [
    "http://localhost:8000",
]

async def startup():
    await database.connect()

async def shutdown():
    await database.disconnect()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[SETUP] running setup...")
    await startup()
    print("[SETUP] completed")
    yield
    await shutdown()

# FastAPI app instance
app = FastAPI(
    title="Order API's",
    description="Order API's",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

metadata.create_all(engine)

# routes
app.include_router(router)
