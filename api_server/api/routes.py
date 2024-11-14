from fastapi import (
    APIRouter,
)
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get("/health", tags=["root"])
def get_health():
    return JSONResponse(
        content={
            "data": "server is up and running"
        },
        status_code=200
    )