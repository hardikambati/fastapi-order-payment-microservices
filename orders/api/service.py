import uuid

from fastapi import (
    HTTPException,
)
from sqlalchemy.orm import Session

from .models import (
    Order,
    OrderProduct,
)


class OrderService:
    """order specific services"""

    def __init__(self, db: Session):
        self.db = db

    def create_order(self, payload: dict) -> dict:
        # create order
        query = Order(
            user_id=payload.user_id,
            reference_key=str(uuid.uuid4()),
            total_amount=payload.total_amount,
            status="pending",
        )
        self.db.add(query)

        # create order products
        # TODO : validate each product by hittin request to product service
        product_list = []
        order_product_list = [
            OrderProduct(order_id=query.id, product_id=product.id)
            for product in product_list
        ]
        self.db.bulk_save_objects(order_product_list)
        self.db.commit()
        self.db.refresh(query)

        response = vars(query)
        response["products"] = product_list
        return response

    def get_all_orders(self, user_id: int) -> dict:
        order_query = self.db.query(Order).filter(
            Order.user_id == user_id
        ).first()
        if not order_query:
            raise HTTPException(detail="Invalid order ID", status_code=404)
        
        order_product_query = self.db.query(OrderProduct).filter(
            OrderProduct.order_id == order_query.id and
            OrderProduct.user_id == user_id
        )

        # TODO : validate each product by hittin request to product service
        products_list = []

        response = vars(order_query)
        response["products"] = products_list
        return response
    
    def get_single_order(self, order_id: int):
        order_query = self.db.query(Order).filter(
            Order.id == order_id
        ).first()
        if not order_query:
            raise HTTPException(detail="Invalid order ID", status_code=404)
        
        order_product_query = self.db.query(OrderProduct).filter(
            OrderProduct.order_id == order_query.id
        )

        # TODO : validate each product by hittin request to product service
        products_list = []

        response = vars(order_query)
        response["products"] = products_list
        return response