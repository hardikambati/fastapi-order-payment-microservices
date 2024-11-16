from typing import List
from pydantic import (
    Field,
    BaseModel,
)
from datetime import datetime


class ProductSchema(BaseModel):
    description: str = Field(...)
    price: float = Field(...)


class ProductDetailSchema(ProductSchema, BaseModel):
    id: int = Field(...)
    created_at: datetime = Field(...)