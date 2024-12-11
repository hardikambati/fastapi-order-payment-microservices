from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from api import models
from db import (
    engine,
    database,
    metadata,
)
from alembic import command
from alembic.config import Config


# accept connections from
origins = [
    "http://localhost:8000",
]

# FastAPI app instance
async def startup():
    # TODO : automate migrations
    # alembic_config = Config("alembic.ini")
    # command.upgrade(alembic_config, "head")
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

app = FastAPI(
    title="Order Payment Interface",
    description="API's that function using microservice architecture",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# metadata.create_all(engine)
models.Base.metadata.create_all(bind=engine)

# routes
app.include_router(router)
