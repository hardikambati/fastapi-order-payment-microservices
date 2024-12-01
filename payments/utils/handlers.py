import time

from utils import decorators


@decorators.validate_order_data
def handle_order_payment(*args, **kwargs):
    """Order payment handler"""

    print("[EVENT] received following message from channel : {}")
    time.sleep(5)
    print("[EVENT] payment successful")

    # call update payment from paymentservice