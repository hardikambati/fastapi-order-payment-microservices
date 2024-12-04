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
)
from helpers.validators import (
    validate_user_key,
)
from .service import UserService


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
async def post_order(key: str = Depends(validate_user_key), db: Session = Depends(get_db)):
    """create order"""
    pass


@router.get("/orders", tags=["Order"])
async def get_orders(key: str = Depends(validate_user_key), db: Session = Depends(get_db)):
    """get all orders"""
    pass


@router.get("/orders/{id}", tags=["Order"])
async def get_single_order(id: int, key: str = Depends(validate_user_key), db: Session = Depends(get_db)):
    """get single order"""
    pass


# =============== PRODUCTS ===============


@router.get("/products", tags=["Product"])
async def get_products(key: str = Depends(validate_user_key), db: Session = Depends(get_db)):
    """get all products"""
    pass
