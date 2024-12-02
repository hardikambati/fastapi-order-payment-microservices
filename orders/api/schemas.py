from typing import List
from pydantic import (
    Field,
    BaseModel,
)


class OrderRequestSchema(BaseModel):
    user_id: int = Field(...)
    product_ids: List[int] = Field(...)


class OrderUpdateSchema(BaseModel):
    order_id: int = Field(...)
    status: str = Field(...)
