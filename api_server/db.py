import os
from sqlalchemy import (
    MetaData,
    create_engine,
)
from datetime import datetime
from databases import Database


DATABASE_URL = os.getenv("DATABASE_URL")

# create engine
metadata = MetaData()
engine = create_engine(DATABASE_URL)
database = Database(DATABASE_URL)
