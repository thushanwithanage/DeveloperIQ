from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.errors import PyMongoError

from models.UserStats import UserStats
from utils.config import database_url
from utils.constants import database_name,stats_collection_name

def save_dev_stats(userStats: UserStats):
    try:
        #print(userStats)
        client = MongoClient(database_url)
        db = client[database_name]
        collection = db[stats_collection_name]

        userStats["_id"] = ObjectId()
        result = collection.insert_one(userStats)

        return result.acknowledged
    except PyMongoError as e:
        print(e)
        return False
    except Exception as e:
        print(e)
        return False
    finally:
        client.close()