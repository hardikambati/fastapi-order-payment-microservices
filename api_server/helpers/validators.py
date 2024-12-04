from fastapi import (
    Query,
)


async def validate_user_key(key: str = Query(max_length=50)):
    # TODO : check key validation
    user_key = None
    return user_key
