from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str


@app.get("/")
def read_root():
    return {"Hello":"World"}

