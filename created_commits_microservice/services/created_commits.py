from datetime import datetime, timedelta

#Filter the no. of commits created by user on the previous date
def filter_commits(commits, username):
    count = 0
    for commit in commits:
        commit_date = datetime.strptime(commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ").date()
        current_date = datetime.utcnow().date()
        if commit["author"]["name"] == username and commit_date == current_date-timedelta(days=1):
            count = count+1
    return count