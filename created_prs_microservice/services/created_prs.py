from datetime import datetime, timedelta

#Filter the no. of commits created by user on the previous date
def filter_prs(prs, username):
    count = 0
    for pr in prs:
        pr_date = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ").date()
        current_date = datetime.utcnow().date()
        #if pr["user"]["login"] == username and pr_date == current_date-timedelta(days=1):
        if pr["user"]["login"] == username and pr_date == current_date:
            count = count+1
    return count