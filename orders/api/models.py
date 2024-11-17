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
from sqlalchemy.orm import relationship


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

    # relationship to OrderProduct
    products = relationship("OrderProduct", backref="order")

    def __repr__(self):
        return f"{self.reference_key}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "reference_key": self.reference_key,
            "total_amount": self.total_amount,
            "status": self.status,
            "created_at": self.created_at,
        }

    def get_product_ids(self) -> list:
        values = [product.product_id for product in self.products]
        return values


class OrderProduct(Base):
    __tablename__ = "OrderProduct"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("Orders.id"), nullable=False)
    product_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"{self.order_id}_{self.product_id}"
