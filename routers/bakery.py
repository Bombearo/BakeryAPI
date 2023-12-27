from fastapi import APIRouter, HTTPException
from database import get_bakery_db
from models import TreatModel

router = APIRouter(
    prefix="/bakery",
    tags=["bakery"],
)

db = get_bakery_db()

@router.get("/")
async def get_bakery_info():
    return {"Name":"Bakery!"}

@router.get("/products",
            response_description="List all treats",
)
async def get_products():
    treats = db.get_collection("treats")
    model = TreatModel(treats= treats.find())
    return model.treats


@router.get("/products/{productID}")
async def get_products_by_ID(productID):
    treat =  db.treats.find_one({"_id":productID})
    if treat:
        return treat
    
    raise HTTPException(status_code=404) 

