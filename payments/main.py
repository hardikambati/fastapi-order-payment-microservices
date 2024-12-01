import asyncio
from fastapi import (
    FastAPI
)
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router
from core.main import subscribe
from payments.utils.handlers import handle_order_payment
from core.utils.redis.channels_enum import (
    BaseChannelEnum,
)
from db import (
    engine,
    database,
    metadata,
)


# accept connections from
origins = [
    "http://localhost:8000",
]

async def listen_to_redis_channel():
    subscribe(BaseChannelEnum.PAYMENT.value, handle_order_payment)

async def startup():
    asyncio.create_task(listen_to_redis_channel())
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
    title="Payment API's",
    description="Payment API's",
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
