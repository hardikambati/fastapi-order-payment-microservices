from fastapi import FastAPI

from api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from db import (
    engine,
    database,
    metadata,
)
from alembic import command
from alembic.config import Config

metadata.create_all(engine)

# accept connections from
origins = [
    "http://localhost:8000",
]

# FastAPI app instance
app = FastAPI(
    title="Order Payment Interface",
    description="API's that function using microservice architecture",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    # TODO : automate migrations
    # alembic_config = Config("alembic.ini")
    # command.upgrade(alembic_config, "head")
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# routes
app.include_router(router)
