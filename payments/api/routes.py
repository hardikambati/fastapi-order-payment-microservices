from fastapi import (
    Depends,
    APIRouter,
)
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from db import get_db
from .schemas import (
    PaymentSchema,
)
from .service import (
    PaymentService,
)


router = APIRouter()


@router.get("/payments/health", tags=["System health"])
def get_health():
    return JSONResponse(
        content={
            "data": "server is up and running"
        },
        status_code=200
    )


@router.get("/payments/{id}", response_model=PaymentSchema, tags=["Payment"])
async def get_payment(id: int, db: Session = Depends(get_db)):
    """get payment info"""
    query = PaymentService(db=db).get_payment(id=id)
    return query
    