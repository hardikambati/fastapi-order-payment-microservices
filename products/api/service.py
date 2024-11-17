from fastapi import (
    HTTPException,
)
from sqlalchemy.orm import Session

from .models import Product
from .schemas import (
    ProductSchema,
    ProductRequestSchema,
)


class ProductService:
    """product specific services"""

    def __init__(self, db: Session):
        self.db = db

    def create_product(self, payload: ProductSchema):
        query = Product(description=payload.description, price=payload.price)
        self.db.add(query)
        self.db.commit()
        return query

    def get_all_products(self):
        query = self.db.query(Product).all()
        return query
    
    def get_particulars(self, payload: ProductRequestSchema):
        query = self.db.query(Product).filter(
            Product.id.in_(payload.product_ids)
        )
        return query