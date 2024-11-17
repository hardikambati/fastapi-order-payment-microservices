from typing import (
    Union,
)
from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
)
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from db import get_db
from .schemas import (
    OrderRequestSchema,
)
from .service import OrderService


router = APIRouter()


@router.get("/orders/health", tags=["System health"])
def get_health():
    return JSONResponse(
        content={
            "data": "server is up and running"
        },
        status_code=200
    )


@router.post("/orders", tags=["Order"])
async def post_order(payload: OrderRequestSchema, db: Session = Depends(get_db)):
    """create an order"""
    query = OrderService(db).create_order(payload)
    return query


@router.get("/orders", tags=["Order"])
async def get_all_orders(user_id: Union[int], db: Session = Depends(get_db)):
    """get list of all order for a user"""
    if not user_id:
        raise HTTPException("Required user_id as a param")
    query = OrderService(db).get_all_orders(user_id)
    return query


@router.get("/orders/{id}", tags=["Order"])
async def get_single_order(id: int, db: Session = Depends(get_db)):
    """get single product"""
    query = OrderService(db).get_single_order(id)
    return query

