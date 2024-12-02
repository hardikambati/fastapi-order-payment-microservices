from fastapi import (
    HTTPException,
)

from core.utils.redis.events import (
    event_exists,
    PaymentEventEnum,
)


def validate_order_data(func):
    """validates order data"""
    def wrapper(*args, **kwargs):
        event = args[0].get("event")
        data = args[0].get("data")

        event_exists_status: bool = event_exists(PaymentEventEnum, event)
        if not event_exists_status:
            # TODO : log errors
            raise HTTPException(detail=f"Event not found : {event}", status_code=404)

        order_id: int = data.get("order_id")
        user_id: int = data.get("user_id")
        total_amount: float = data.get("total_amount")

        if not (
            order_id or user_id or total_amount
        ):
            raise HTTPException(detail="Invalid data", status_code=400)
        return func(*args, **kwargs)
    return wrapper
