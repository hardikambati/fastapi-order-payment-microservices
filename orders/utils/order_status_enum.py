from enum import Enum

STATUSES = [
    "init",
    "pending",
    "successful", 
    "failed"
]


class OrderStatusEnum(Enum):
    """order status mapping"""

    INIT = "init"
    PENDING = "pending"
    SUCCESS = "successful"
    FAILED = "failed"

