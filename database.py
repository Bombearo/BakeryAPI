from pymongo import MongoClient
import os
import certifi

#Setup MongoDB
PWD = os.getenv("MONGO_PWD")
filepath = os.getenv("FOLDER")
connection_string = f"mongodb+srv://Jaden:{PWD}@bakerytreats.txkm7zv.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tlsCAFile=certifi.where())


def get_bakery_db():
    return client.bakery