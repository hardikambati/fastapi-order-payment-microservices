import uuid

from sqlalchemy import (
    Float,
    String,
    Column,
    Integer,
    DateTime,
    ForeignKey,
)
from datetime import datetime
import sqlalchemy.orm


Base = sqlalchemy.orm.declarative_base()


def generate_key() -> str:
    key = str(uuid.uuid4())
    return key

class Payment(Base):
    __tablename__ = "Payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_amount = Column(Float, nullable=False)
    reference_key = Column(String, nullable=False, default=generate_key)
    # status_list : [processing, successful, failed]
    status = Column(String, nullable=False, default="processing")
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"{self.reference_key}"


class OrderPayment(Base):
    __tablename__ = "OrderPayment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    order_id = Column(Integer, nullable=False)
    payment_id = Column(Integer, ForeignKey("Payments.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"{self.payment_id}"
