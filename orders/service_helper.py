from enum import Enum


class ServiceEnum(Enum):
    """Enum with all services"""

    # service name = (name, port)
    API_SERVER = ("api_server", 8000)
    PRODUCT = ("products", 8001)
    ORDER = ("orders", 8002)
    PAYMENT = ("payment", 'xxx')


def get_domain(service: ServiceEnum) -> str:
    service_value = service.value
    return f"http://{service_value[0]}:{service_value[1]}"
