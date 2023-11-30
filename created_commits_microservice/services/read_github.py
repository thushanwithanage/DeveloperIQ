import requests

#Get all issues/commits
def get_github_data(url, headers):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch issues. Status code: {response.status_code}")
        return -1