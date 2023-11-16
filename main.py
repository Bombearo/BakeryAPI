from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv
import certifi

#Setup ENV Vars
load_dotenv(find_dotenv())

#Setup MongoDB
PWD = os.getenv("MONGO_PWD")
connection_string = f"mongodb+srv://Jaden:{PWD}@bakerytreats.txkm7zv.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tlsCAFile=certifi.where())




app = FastAPI()

class Item(BaseModel):
    name: str


@app.get("/")
def read_root():
    return {"Hello":"World"}


