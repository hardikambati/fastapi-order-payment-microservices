from typing import List
from fastapi import (
    Depends,
    APIRouter,
)
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


from db import get_db
from .schemas import (
    ProductSchema,
    ProductDetailSchema,
)
from .service import ProductService


router = APIRouter()


@router.get("/products/health", tags=["System health"])
def get_health():
    return JSONResponse(
        content={
            "data": "server is up and running"
        },
        status_code=200
    )


@router.post("/products", response_model=ProductDetailSchema, tags=["Product"])
async def post_product(payload: ProductSchema, db: Session = Depends(get_db)):
    """create a product"""
    query = ProductService(db).create_product(payload)
    return query


@router.get("/products", response_model=List[ProductDetailSchema], tags=["Product"])
async def get_all_products(db: Session = Depends(get_db)):
    """get list of all products"""
    query = ProductService(db).get_all_products()
    return query


@router.get("/products/{id}", response_model=ProductDetailSchema, tags=["Product"])
async def get_single_product(id: int, db: Session = Depends(get_db)):
    """get single product"""
    query = ProductService(db).get_single_product(id)
    return query

