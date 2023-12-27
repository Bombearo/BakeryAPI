from pydantic import BaseModel
from typing import List

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


class Ingredient(BaseModel):
    name:str
    quantity:int
    price_per_gram:float

class Treat(BaseModel):
    name: str
    ingredients:List[Ingredient] | None = None

class TreatModel(BaseModel):
    treats: List[Treat]
    
