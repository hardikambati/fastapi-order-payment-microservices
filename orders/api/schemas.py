from typing import (
    List,
    Literal,
)
from pydantic import (
    BaseModel,
)


class OrderRequestSchema(BaseModel):
    user_id: int
    product_ids: List[int]


class OrderUpdateSchema(BaseModel):
    order_id: int
    status: Literal["SUCCESS", "FAILURE"]
