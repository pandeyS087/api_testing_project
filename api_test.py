import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_status_code():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_data_exists():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "userId" in data

def test_first_post_title():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert len(data["title"]) > 0