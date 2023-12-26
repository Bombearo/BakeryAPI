from fastapi import APIRouter


router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"],
)


@router.get("/")
async def get_details():

    return {"a":"b"}
