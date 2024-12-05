from fastapi import (
    Query,
    Depends,
    HTTPException,
)
from api.models import (
    User,
)
from db import get_db
from sqlalchemy.orm import (
    Session,
)


async def validate_user_key(key: str = Query(max_length=50), db: Session = Depends(get_db)) -> str:
    """checks user unique key validation"""
    query = db.query(User).filter(
        User.unique_id == key
    ).first()
    if not query:
        raise HTTPException(detail="Invalid key", status_code=400)
    return query.id
