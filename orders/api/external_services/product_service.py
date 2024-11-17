import json

import requests

from service_helper import (
    get_domain,
    ServiceEnum,
)


class ProductService:
    """get data from product service"""

    def get_all_products(self, product_ids: list):
        response = requests.post(
            url=get_domain(ServiceEnum.PRODUCT) + "/products/particulars",
            headers={"Content-Type": "application/json"},
            json={
                "product_ids": product_ids
            }
        )
        return json.loads(response.content.decode())
