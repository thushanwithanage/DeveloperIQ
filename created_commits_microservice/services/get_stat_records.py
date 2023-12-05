from pymongo import MongoClient
from pymongo.errors import PyMongoError
import json

from models.UserStats import UserStats
from utils.constants import database_name,stats_collection_name
from utils.filter_query import get_filter_query
from services.fetch_mongodb_secret import get_secret

def get_monthly_stats(userId):
    try:
        db_url = get_secret()
        client = MongoClient(db_url)
        db = client[database_name]
        collection = db[stats_collection_name]

        filter_query = get_filter_query(userId)

        stats = []
        for document in collection.find(filter_query):
            stat = UserStats(
                username=document["username"],
                user_id=document["user_id"],
                stat_type=document["stat_type"],
                count=document["count"],
                date_value=document["date_value"]
            )
            stats.append(stat)
        return json.dumps([stat.json() for stat in stats])
    except PyMongoError as e:
        print(e)
        return []
    except Exception as e:
        print(e)
        return []
    finally:
        client.close()