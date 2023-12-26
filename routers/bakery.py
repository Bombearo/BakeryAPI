from fastapi import APIRouter


router = APIRouter(
    prefix="/bakery",
    tags=["bakery"],
)

@router.get("/")
async def get_bakery_info():
    return {}

@router.get("/products")
async def get_products():
    return []


@router.get("/products/{productID}")
async def get_products_by_ID(productID):
    return {}
