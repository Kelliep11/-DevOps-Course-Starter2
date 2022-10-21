import pymongo
import os
from todo_app.data.item import Item

def get_items():
    client = pymongo.MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
    database = client[os.getenv("MONGO_DATABASE_NAME")]
    collection = database["items"]
    
    mongo_items = collection.find()

    return [Item.from_mongo_item(mongo_item) for mongo_item in mongo_items]

def add_items(title: str):
    new_mongo_item = {
        'task': title,
        'status': "To Do"
    }

    client = pymongo.MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
    database = client[os.getenv("MONGO_DATABASE_NAME")]
    collection = database["items"]
    collection.insert_one(new_mongo_item)

   
def complete_item(mongo_id):
    client = pymongo.MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
    database = client[os.getenv("MONGO_DATABASE_NAME")]
    collection = database["items"]

    myquery = { "_id": mongo_id }
    newvalues = { "$set": { "status": "Done" } }

    collection.update_one(myquery, newvalues)