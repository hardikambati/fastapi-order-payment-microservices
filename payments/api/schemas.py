from datetime import datetime
from pydantic import (
    BaseModel,
)


class PaymentSchema(BaseModel):
    id: int
    total_amount: float
    reference_key: str
    status: str
    created_at: datetime
