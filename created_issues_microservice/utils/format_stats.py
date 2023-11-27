from utils.date_utils import last_date
from utils.constants import stat_type

def format_developer_stats(userName,userId,created_issues_count):
    developer_stats = {
            "username": userName,
            "user_id": userId,
            "stat_type": "created_issues",
            "count": created_issues_count,
            "date_value": last_date
        }
    return developer_stats