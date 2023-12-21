import requests
import json

base_url = "http://aba7c0ccb12bf4b8b9b4d57dade32948-906313938.ap-south-1.elb.amazonaws.com:8081" #Update

def test_root_endpoint():
    response = requests.get(f"{base_url}/")
    assert response.status_code == 200
    assert response.json() == {"response": "Github created issues route"}

def test_read_users():
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    for item_str in response.json():
        item = json.loads(item_str)
        assert "user_id" in item
        assert "username" in item

        assert isinstance(item["user_id"], int)
        assert isinstance(item["username"], str)

def test_created_issues():
    user = "thushaniit"
    response = requests.get(f"{base_url}/created_issues/{user}")
    assert response.status_code == 200
    assert isinstance(response.json(), int)

def test_get_dev_monthly_stats():
    response = requests.get(f"{base_url}/monthly_stats")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
    for item in response.json():
        assert "user_id" in item
        assert "username" in item
        assert "count" in item

        assert isinstance(item["user_id"], int)
        assert isinstance(item["username"], str)
        assert isinstance(item["count"], int)