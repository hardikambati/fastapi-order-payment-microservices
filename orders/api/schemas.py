from typing import (
    List,
    Literal,
)
from pydantic import (
    BaseModel,
)
from core.utils.helpers.status import WebhookStatusEnum


class OrderRequestSchema(BaseModel):
    user_id: int
    product_ids: List[int]


class OrderUpdateSchema(BaseModel):
    order_id: int
    status: WebhookStatusEnum
