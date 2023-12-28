from models.general import MongoModel
from typing import List


class Experience(MongoModel):
    startYear: str
    endYear: str
    title: str
    description: str
