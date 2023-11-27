from fastapi import FastAPI
import uvicorn
import json

from services.get_user_records import get_users
from services.save_record import save_dev_stats
from services.read_github import get_github_data
from services.filter_prs import filter_out_prs
from services.created_issues import filter_created_issues

from services.format_response import format_user_response, format_user_stats_response

from utils.config import headers
from utils.constants import created_issues_url
from utils.format_stats import format_developer_stats

from models.UserStats import UserStats

app = FastAPI()

@app.get("/")
async def root():
    return {"response": "Github created issues route"}

@app.get("/users")
async def read_users():
    users = get_users()
    return json.loads(users)

@app.get("/created_issues/{user}")
async def created_issues(user: str):
    all_issues = get_github_data(created_issues_url+user, headers)
    created_issues = filter_out_prs(all_issues)
    created_issue_count_by_user = filter_created_issues(created_issues, user)
    return json.loads(str(created_issue_count_by_user))

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
        created_issues_count = await created_issues(uname)
        developer_stats = format_developer_stats(uname,uid,created_issues_count)
        save_stats_list.append(await save_stat(developer_stats))
    insert_status_data = format_user_stats_response(user_id_list, save_stats_list)
    return insert_status_data

if __name__ == "__main__":
    uvicorn.run(app, port=8081, host="0.0.0.0")