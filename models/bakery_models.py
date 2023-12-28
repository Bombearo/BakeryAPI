from pydantic import BaseModel
from typing import List


class Ingredient(BaseModel):
    name: str
    quantity: int
    price_per_gram: float


class Treat(BaseModel):
    name: str
    ingredients: List[Ingredient] | None = None


class TreatModel(BaseModel):
    treats: List[Treat]
