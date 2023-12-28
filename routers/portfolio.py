from fastapi import APIRouter, Depends
from database import get_portfolio_db
from utils.security import get_current_active_user
from models.portfolio_models import Experience
from models.users import User

from typing import Annotated

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"],
)

db = get_portfolio_db()

@router.get("/")
async def get_details():

    return {"a":"b"}



@router.get("/experience")
async def get_experience():
    experience_collection = db.get_collection("experience")

    return {}

@router.post("/experience/addExperience")
async def add_experience(experience: Experience, current_user:Annotated[User, Depends(get_current_active_user)]):
    print(experience)

    return {}