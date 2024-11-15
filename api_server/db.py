import os
from sqlalchemy import (
    MetaData,
    create_engine,
)
from databases import Database
from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.getenv("DATABASE_URL")

# create engine
metadata = MetaData()
engine = create_engine(DATABASE_URL)
database = Database(DATABASE_URL)

# session maker
SessionLocal = sessionmaker(autoflush=False, bind=engine)

def get_db():
    """create database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
