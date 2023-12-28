from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from database import get_portfolio_db
from utils.security import get_current_active_user
from models.portfolio_models import Experience
from models.general import User

from typing import Annotated, List

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"],
)

db = get_portfolio_db()

@router.get("/")
async def get_details():

    return {"a":"b"}



@router.get("/experience", response_model=List[Experience])
async def get_experience():
    """
    GET Request - Retrieves all experience from the MongoDB
    """
    experience_collection = db.get_collection("experience")
    a = [experience for experience in experience_collection.find()]
    print (a)
    return a

@router.post("/experience",
             response_model=Experience)
async def add_experience(experience: Experience, current_user:Annotated[User, Depends(get_current_active_user)]):

    experience = jsonable_encoder(experience)
    if current_user.username == "Admin":
        new_experience = db.experience.insert_one(experience)
        created = db.experience.find_one({"_id":new_experience.inserted_id})

        return created
    return {}