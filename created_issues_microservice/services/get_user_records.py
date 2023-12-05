from pymongo import MongoClient
from pymongo.errors import PyMongoError
import json

from models.User import User
from utils.constants import database_name,user_collection_name
from services.fetch_mongodb_secret import get_secret

def get_users():
    try:
        client = None
        db_url = get_secret()
        client = MongoClient(db_url)
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