import time


def handle_order_payment(data: dict, *args, **kwargs):
    """Order payment handler"""

    print("[PAYMENT] initiating payment...")
    print(data)
    time.sleep(5)
    print("[PAYMENT] payment successful")

    # call update payment from paymentservice