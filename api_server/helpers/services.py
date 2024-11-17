from enum import Enum


class ServiceEnum(Enum):
    """Enum with all services"""

    # service name = (name, port)
    API_SERVER = ("api_server", 8000)
    PRODUCT = ("product", 8001)
    ORDER = ("order", 8002)
    PAYMENT = ("payment", 'xxx')
