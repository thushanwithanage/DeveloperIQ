from fastapi import FastAPI
import uvicorn
import json

from services.get_user_records import get_users
from services.get_stat_records import get_monthly_stats
from services.save_record import save_dev_stats
from services.read_github import get_github_data
from services.created_prs import filter_prs

from services.format_response import format_user_response, format_user_stats_response

from utils.config import headers
from utils.constants import created_prs_url
from utils.format_stats import format_developer_stats, format_monthly_stats, format_final_stats

from models.UserStats import UserStats

app = FastAPI()

@app.get("/")
async def root():
    return {"response": "Github created prs route"}

@app.get("/users")
async def read_users():
    users = get_users()
    return json.loads(users)

@app.get("/created_prs/{user}")
async def created_prs(user: str):
    all_prs = get_github_data(created_prs_url, headers)
    created_prs_count_by_user = filter_prs(all_prs, user)
    return json.loads(str(created_prs_count_by_user))

@app.post("/insert")
async def save_stat(userStats: UserStats):
    status = save_dev_stats(userStats)
    return json.dumps(status)

@app.get("/save_stats")
async def save_user_stats():
    users = await read_users()
    user_id_list, username_list = format_user_response(users)
    save_stats_list = []
    for uid, uname in zip(user_id_list, username_list):
        created_prs_count = await created_prs(uname)
        developer_stats = format_developer_stats(uname,uid,created_prs_count)
        save_stats_list.append(await save_stat(developer_stats))
    insert_status_data = format_user_stats_response(user_id_list, save_stats_list)
    return insert_status_data

@app.get("/monthly_stats")
async def get_dev_monthly_stats():
    users = await read_users()
    user_id_list, username_list = format_user_response(users)
    userStats = []
    for uid, uname in zip(user_id_list, username_list):
        monthly_entries = json.loads(get_monthly_stats(str(uid)))
        total_count = format_monthly_stats(monthly_entries)
        userStats.append(format_final_stats(uid, uname, total_count))
    return userStats

if __name__ == "__main__":
    uvicorn.run(app, port=8084, host="0.0.0.0")