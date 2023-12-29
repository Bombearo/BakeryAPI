from pydantic import BaseModel
from typing import List
from beanie import Document


class Ingredient(BaseModel):
    name: str
    quantity: int
    price_per_gram: float


class Treat(Document):
    name: str
    ingredients: List[Ingredient] | None = None

    class Settings:
        name = "treats"


class TreatModel(BaseModel):
    treats: List[Treat]
