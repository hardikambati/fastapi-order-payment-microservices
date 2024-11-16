# consists of all main operations
import uuid

from fastapi import (
    HTTPException,
)
from sqlalchemy.orm import Session

from .models import User


class UserService:
    """user specific services"""

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, payload: dict):
        query = User(name=payload.name, unique_id=str(uuid.uuid4()))
        self.db.add(query)
        self.db.commit()
        return query
    
    def get_user(self, unique_id):
        query = self.db.query(User).filter(
            User.unique_id == unique_id
        ).first()
        if query:
            return query
        raise HTTPException(detail="Invalid unique_id", status_code=404)

    def get_all_users(self):
        query = self.db.query(User).all()
        return query