import time

from db import get_db

from utils import decorators
from api.service import PaymentService
from db import SessionLocal
from core.utils.external_services.orders import (
    OrderService,
)
from core.utils.redis.channels import (
    BaseChannelEnum,
)


@decorators.validate_order_data
async def handle_order_payment(data: dict, *args, **kwargs):
    """Order payment handler"""

    print(f"[EVENT] received following message from channel : {BaseChannelEnum.PAYMENT.value}")
    print(data)
    # db session
    db = SessionLocal()

    # create payment
    PaymentService(db=db).create_payment(data=data["data"])
    
    # call order webhook
    response = OrderService().update_order_status(order_id=data["data"]["order_id"])
    response_detail = response.get("detail")
    print(f"[WEBHOOK EVENT] {response_detail}")

    db.close()

    print("[EVENT] payment successful")
