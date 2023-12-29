from pymongo import MongoClient
import os
import certifi
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.portfolio_models import *
from models.bakery_models import *

#Setup MongoDB
async def init_db():
    PWD = os.getenv("MONGO_PWD")
    connection_string = f"mongodb+srv://Jaden:{PWD}@bakerytreats.txkm7zv.mongodb.net/?retryWrites=true&w=majority"
    client = AsyncIOMotorClient(connection_string, tlsCAFile=certifi.where())
    return client


async def get_bakery_db(client):
    await init_beanie(database=client.bakery, document_models=[Treat])

async def get_portfolio_db(client):
    await init_beanie(database=client.portfolio, document_models=[Experience])