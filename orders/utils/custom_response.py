from fastapi.responses import JSONResponse


def WebhookResponse(detail: str, status_code: int):
    return JSONResponse(
        content={
            "detail": detail
        },
        status_code=status_code
    )
