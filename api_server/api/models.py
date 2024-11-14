from sqlalchemy import (
    String,
    Column,
    Integer,
    DateTime,
)
from datetime import datetime
import sqlalchemy.orm


Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    unique_id = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"{self.name}_{self.unique_id}"
