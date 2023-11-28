#from utils.date_utils import first_day_of_month, last_day_of_month
from utils.constants import stat_type

from datetime import datetime, timedelta

current_date = datetime.now()
first_day_of_month = current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
last_day_of_month = (current_date.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

def get_filter_query(user_id):
    uid = int(user_id)
    query = {
    "user_id": uid,
    "date_value": {"$gte": str(first_day_of_month), "$lte": str(last_day_of_month)},
    "stat_type":stat_type
}
    return query