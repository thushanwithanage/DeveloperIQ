from pymongo import MongoClient
from pymongo.errors import PyMongoError
import json

from models.User import User
from utils.config import database_url
from utils.constants import database_name,user_collection_name

def get_users():
    try:
        client = MongoClient(database_url)
        db = client[database_name]
        collection = db[user_collection_name]

        users = []
        for document in collection.find():
            user = User(
                username=document["username"],
                user_id=document["user_id"]
            )
            users.append(user)
        return json.dumps([user.json() for user in users])
    except PyMongoError as e:
        print(e)
        return []
    except Exception as e:
        print(e)
        return []
    finally:
        client.close()