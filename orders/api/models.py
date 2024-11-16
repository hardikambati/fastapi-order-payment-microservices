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


class Order(Base):
    __tablename__ = "Orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    reference_key = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)
    # status list : [init, pending, successful, failed]
    status = Column(String, default="init")
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"{self.order_id}"


class OrderProduct(Base):
    __tablename__ = "OrderProduct"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("Orders.id"), nullable=False)
    product_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"{self.order_id}_{self.product_id}"

