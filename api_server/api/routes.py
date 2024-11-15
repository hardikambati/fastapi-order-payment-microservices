import uuid

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
    query = User(name=payload.name, unique_id=str(uuid.uuid4()))
    db.add(query)
    db.commit()
    db.refresh(query)
    return query

@router.get("/user/{unique_id}", response_model=UserDetailsSchema, tags=["User"])
async def get_user(unique_id: str, db: Session = Depends(get_db)) -> UserDetailsSchema:
    """get user details"""
    query = db.query(User).filter(
        User.unique_id == unique_id
    ).first()
    if query:
        return query
    raise HTTPException(detail="Invalid unique_id", status_code=404)

