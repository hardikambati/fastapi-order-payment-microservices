
from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
)
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


from .models import User
from db import get_db
from .schemas import (
    UserSchema,
    UserDetailsSchema,
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

@router.post("/user", response_model=UserDetailsSchema, tags=["User"])
async def post_user(payload: UserSchema, db: Session = Depends(get_db)) -> UserSchema:
    """create user"""
    user = UserService(db).create_user(payload)
    return user

@router.get("/user/{unique_id}", response_model=UserDetailsSchema, tags=["User"])
async def get_user(unique_id: str, db: Session = Depends(get_db)) -> UserDetailsSchema:
    """get user details"""
    user = UserService(db).get_user(unique_id)
    return user

