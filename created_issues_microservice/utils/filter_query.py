from utils.date_utils import first_day_of_month, last_day_of_month
from utils.constants import stat_type

def get_filter_query(user_id):
    uid = int(user_id)
    query = {
    "user_id": uid,
    "date_value": {"$gte": str(first_day_of_month), "$lte": str(last_day_of_month)},
    "stat_type":stat_type
}
    return query