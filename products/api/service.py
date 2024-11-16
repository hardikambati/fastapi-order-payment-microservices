from fastapi import (
    HTTPException,
)
from sqlalchemy.orm import Session

from .models import Product


class ProductService:
    """product specific services"""

    def __init__(self, db: Session):
        self.db = db

    def create_product(self, payload: dict):
        query = Product(description=payload.description, price=payload.price)
        self.db.add(query)
        self.db.commit()
        return query

    def get_all_products(self):
        query = self.db.query(Product).all()
        return query
    
    def get_single_product(self, product_id: int):
        query = self.db.query(Product).filter(
            Product.id == product_id
        ).first()
        if query:
            return query
        raise HTTPException(detail="Invalid product id", status_code=404)