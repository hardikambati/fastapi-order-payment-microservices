from sqlalchemy.orm import (
    Session,
)


class PaymentService:
    """payment specific services"""

    def __init__(self, db: Session):
        self.db = db

    def get_payment(self, id):
        pass

    def update_payment(self, id):
        pass
    