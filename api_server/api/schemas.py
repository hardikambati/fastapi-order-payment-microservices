from pydantic import (
    Field,
    BaseModel,
)


class UserSchema(BaseModel):
    name: str = Field(...)


class UserDetailsSchema(BaseModel):
    name: str = Field(...)
    unique_id: str = Field(...)
