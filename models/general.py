from typing import List, Optional
from pydantic import BaseModel, Field


class ObjectId(BaseModel):
    oid: str


class MongoModel(BaseModel):
    id: Optional[ObjectId] |None = None


class User(BaseModel):
    username: str
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
