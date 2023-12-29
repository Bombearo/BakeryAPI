from fastapi import APIRouter, HTTPException, Depends
from database import get_bakery_db, init_db
from models.bakery_models import TreatModel, Treat
from models.general import User
from typing import Annotated
from beanie import PydanticObjectId

from utils.security import get_current_active_user

router = APIRouter(
    prefix="/bakery",
    tags=["bakery"],
)

@router.on_event("startup")
async def start_db():
    client = await init_db()
    await get_bakery_db(client)

@router.get("/")
async def get_bakery_info():
    return {"Name":"Bakery!"}

@router.get("/products",
            response_description="List all treats",
)
async def get_products():
    treats = await Treat.find_all().to_list()
    return treats


@router.get("/products/{productID}")
async def get_products_by_ID(productID:PydanticObjectId):
    treat = await Treat.get(productID)
    if treat: 
        return treat
    
    raise HTTPException(status_code=404) 

@router.post("/products/")
async def add_new_product(product: Treat, current_user:Annotated[User,Depends(get_current_active_user)]):
    await product.create()
    return {"message": "Review added successfully"}