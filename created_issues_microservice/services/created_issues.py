from datetime import datetime, timedelta

#Filter the no. of issues created by user on the previous date
def filter_issues(issues, username):
    count = 0
    for issue in issues:
        issue_date = datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ").date()
        current_date = datetime.utcnow().date()
        if issue["user"]["login"] == username and issue_date == current_date-timedelta(days=1):
            count = count+1
    return count