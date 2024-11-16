from typing import List
from pydantic import (
    Field,
    BaseModel,
)


class OrderSchema(BaseModel):
    user_id: int = Field(...)
    reference_key: str = Field(...)
    total_amount: float = Field(...)
    status: str = Field(...)

