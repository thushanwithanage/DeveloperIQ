from utils.date_utils import last_date
from utils.constants import stat_type
import json

def format_developer_stats(userName,userId,created_issues_count):
    developer_stats = {
            "username": userName,
            "user_id": userId,
            "stat_type": stat_type,
            "count": created_issues_count,
            "date_value": last_date
        }
    return developer_stats

def format_monthly_stats(response):
    count = 0
    for entry in response:
        stat = json.loads(entry)
        count = count + int(stat["count"])
    return json.loads(str(count))

def format_final_stats(userId,userName,count):
    stats = {
            "user_id": userId,
            "username": userName,
            "count": count
        }
    return stats