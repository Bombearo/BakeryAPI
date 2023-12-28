from pydantic import BaseModel
from typing import List


class Experience(BaseModel):
    startYear: str
    endYear: str
    title: str
    description: str