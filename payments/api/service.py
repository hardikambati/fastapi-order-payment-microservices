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

    def get_payment(self, id):
        pass

    def create_payment(self, data: dict):
        # create payment record
        payment_query = Payment(
            total_amount=float(data["total_amount"])
        )
    