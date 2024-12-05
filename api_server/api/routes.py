from typing import (
    List,
)
from fastapi import (
    Query,
    Depends,
    APIRouter,
)
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


from db import get_db
from .schemas import (
    UserSchema,
    UserDetailsSchema,
    ProductListSchema,
)
from helpers.validators import (
    validate_user_key,
)
from .service import UserService
from core.utils.external_services.orders import OrderService
from core.utils.external_services.products import ProductService

router = APIRouter()


@router.get("/health", tags=["System health"])
def get_health():
    return JSONResponse(
        content={
            "data": "server is up and running"
        },
        status_code=200
    )

# =============== USERS ===============

@router.post("/users", response_model=UserDetailsSchema, tags=["User"])
async def post_user(payload: UserSchema, db: Session = Depends(get_db)) -> UserSchema:
    """create user"""
    user = UserService(db).create_user(payload)
    return user


@router.get("/users/all", response_model=List[UserDetailsSchema], tags=["User"])
async def get_all_users(db: Session = Depends(get_db)):
    """get all users"""
    users = UserService(db).get_all_users()
    return users


@router.get("/users/all/{unique_id}", response_model=UserDetailsSchema, tags=["User"])
async def get_user(unique_id: str, db: Session = Depends(get_db)) -> UserDetailsSchema:
    """get user details"""
    user = UserService(db).get_user(unique_id)
    return user

# =============== ORDERS ===============

@router.post('/orders/create', tags=["Order"])
async def post_order(payload: ProductListSchema, key: str = Depends(validate_user_key)):
    """create order"""
    data = payload.model_dump()
    data["user_id"] = key
    query = OrderService().create_order(payload=data)
    return query


@router.get("/orders", tags=["Order"])
async def get_orders(key: str = Depends(validate_user_key)):
    """get all orders"""
    params = {
        "user_id": key
    }
    query = OrderService().get_all_orders(params=params)
    return query


@router.get("/orders/{id}", tags=["Order"])
async def get_single_order(id: int, key: str = Depends(validate_user_key)):
    """get single order"""
    query = OrderService().get_single_order(id=id)
    return query


# =============== PRODUCTS ===============


@router.get("/products", tags=["Product"])
async def get_products(key: str = Depends(validate_user_key)):
    """get all products"""
    query = ProductService().get_all_products()
    return query
