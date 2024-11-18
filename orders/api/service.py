import uuid

from fastapi import (
    HTTPException,
)
from sqlalchemy.orm import (
    Session,
    joinedload,
)
from .external_services.product_service import ProductService
from .models import (
    Order,
    OrderProduct,
)
from utils import (
    OrderStatusEnum,
    WebhookResponse,
)
from core.main import publish


class OrderService:
    """order specific services"""

    def __init__(self, db: Session):
        self.db = db

    def create_order(self, payload: dict) -> dict:
        product_list = ProductService().get_all_products(product_ids=payload.product_ids)
        # calculate total
        total_amount = 0
        for product in product_list:
            total_amount += product["price"]

        # create order
        query = Order(
            user_id=payload.user_id,
            reference_key=str(uuid.uuid4()),
            total_amount=total_amount,
            status="pending",
        )
        self.db.add(query)
        self.db.commit()
        self.db.refresh(query)

        # create order products
        order_product_list = [
            OrderProduct(order_id=query.id, product_id=product["id"])
            for product in product_list
        ]
        self.db.bulk_save_objects(order_product_list)
        self.db.commit()

        # publish event to payment queue
        data = {
            "event": "ORDER_CREATED",
            "data": {
                "order_id": query.id,
                "user_id": payload.user_id,
                "total_amount": total_amount,
            }
        }
        publish(data=data, channel="payment")

        response = query.to_dict()
        response["products"] = product_list
        return response

    def get_all_orders(self, user_id: int) -> dict:
        order_query = self.db.query(Order) \
            .options(joinedload(Order.products)) \
            .filter(Order.user_id == user_id) \
            .all()
        
        # create unique product id list
        product_id_list = list(set(product for order in order_query for product in order.get_product_ids()))
        # fetch details from product service
        product_list = ProductService().get_all_products(product_ids=product_id_list)
        # create dict for constructing response
        product_info_dict = {product["id"]: product for product in product_list}

        response = []
        for order in order_query:
            constructor = {
                **order.to_dict(),
                "products": [product_info_dict[product_id] for product_id in order.get_product_ids()],
            }
            response.append(constructor)
        return response
    
    def get_single_order(self, order_id: int) -> dict:
        order_query = self.db.query(Order).filter(
            Order.id == order_id
        ).first()
        if not order_query:
            raise HTTPException(detail="Invalid order ID", status_code=404)
        
        order_product_query = self.db.query(OrderProduct).filter(
            OrderProduct.order_id == order_query.id
        )

        product_id_list = [product.product_id for product in order_product_query]
        product_list = ProductService().get_all_products(product_ids=product_id_list)

        response = order_query.to_dict()
        response["products"] = product_list
        return response


class WebhookService:

    def __init__(self, db: Session):
        self.db = db

    def update_order_status(self, payload):
        order_query = self.db.query(Order).filter(
            Order.id == payload.order_id
        ).first()
        if not order_query:
            raise HTTPException(detail="Invalid order ID", status_code=404)
        order_query.status = OrderStatusEnum(OrderStatusEnum.PENDING.value)
        
        self.db.commit()
        return WebhookResponse(detail="Order updated successfully", status_code=404)
