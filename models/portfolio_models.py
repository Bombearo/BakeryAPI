from beanie import Document
from typing import List


class Experience(Document):
    startYear: str
    endYear: str
    title: str
    description: str

    class Settings:
        name = "experience"
    class Config:
        schema_extra = {
            "example": {
                "startYear": "2021",
                "endYear": "2022",
                "title": "Programmer",
                "description": "Developed programs for X company"
            }
        }