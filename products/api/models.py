from sqlalchemy import (
    Float,
    String,
    Column,
    Integer,
    DateTime,
)
from datetime import datetime
import sqlalchemy.orm


Base = sqlalchemy.orm.declarative_base()


class Product(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"{self.description}"
