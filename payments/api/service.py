from fastapi import (
    HTTPException,
)
from sqlalchemy.orm import (
    Session,
)

from .models import (
    Payment,
    OrderPayment,
)


class PaymentService:
    """payment specific services"""

    def __init__(self, db: Session):
        self.db = db

    def get_payment(self, id: int) -> dict:
        query = self.db.query(Payment).filter(
            Payment.id == id
        ).first()
        if not query:
            raise HTTPException(detail="Invalid payment ID", status_code=400)
        return query

    def create_payment(self, data: dict) -> dict:
        user_id: int = data["user_id"]
        order_id: int = data["order_id"]
        
        # create payment record
        payment_query = Payment(
            total_amount=float(data["total_amount"])
        )
        self.db.add(payment_query)
        self.db.commit()

        # create order payment record
        order_payment_query = OrderPayment(
            user_id=user_id,
            order_id=order_id,
            payment_id=payment_query.id,
        )
    
        self.db.add(order_payment_query)
        self.db.commit()
