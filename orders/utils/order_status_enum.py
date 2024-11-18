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
    SUCCESSFUL = "successful"
    FAILED = "failed"

