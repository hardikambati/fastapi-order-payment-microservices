import time

from core.main import subscribe


def handle_order_payment(data: dict, *args, **kwargs):
    """Order payment handler"""

    print("[PAYMENT] initiating payment...")
    print(data)
    time.sleep(5)
    print("[PAYMENT] payment successful")


subscribe("payment", handle_order_payment)
