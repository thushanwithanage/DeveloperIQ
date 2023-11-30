import json

def format_user_response(response):
    user_id_list = []
    username_list = []
    for entry in response:
        user = json.loads(entry)
        user_id_list.append(user["user_id"])
        username_list.append(user["username"])
    return user_id_list, username_list

def format_user_stats_response(userids, statuses):
    user_data = [{"userId": uids, "status": status} for uids, status in zip(userids, statuses)]
    insert_status_data = json.dumps(user_data)
    return insert_status_data