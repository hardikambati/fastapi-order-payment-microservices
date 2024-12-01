import time

from db import get_db

from utils import decorators
from payments.api.service import PaymentService
from core.utils.external_services.orders import (
    OrderService,
)


@decorators.validate_order_data
def handle_order_payment(data: dict):
    """Order payment handler"""

    print("[EVENT] received following message from channel : {}")
    time.sleep(5)
    # db session
    db = get_db()

    # create payment
    PaymentService(db=db).create_payment(data=data[0])
    # call order webhook
    OrderService().update_order_status(order_id=data[0]["order_id"])

    print("[EVENT] payment successful")
