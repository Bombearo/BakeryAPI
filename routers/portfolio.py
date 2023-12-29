from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from database import get_portfolio_db, init_db
from utils.security import get_current_active_user
from models.portfolio_models import Experience
from models.general import User

from typing import Annotated, List

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"],
)

@router.on_event("startup")
async def start_db():
    client = await init_db()
    await get_portfolio_db(client)

@router.get("/")
async def get_details():

    return {"a":"b"}



@router.get("/experience", response_model=List[Experience])
async def get_experience():
    """
    GET Request - Retrieves all experience from the MongoDB
    """
    data = await Experience.find_all().to_list()
    return data

@router.post("/experience", response_description="Experience added to the Database")
async def add_experience(experience: Experience, current_user:Annotated[User, Depends(get_current_active_user)]):
    if current_user.username == "Admin":
        await experience.create()

        return {"message": "Review added successfully"}
    return {}