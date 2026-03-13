import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def get_posts():
    """Fetch all posts from the API"""
    response = requests.get(BASE_URL)
    return response

def test_status_code(response):
    """Test if API returns status code 200"""
    if response.status_code == 200:
        print("✅ Test Case 1 Passed: Status code 200")
    else:
        print(f"❌ Test Case 1 Failed: Status code {response.status_code}")

def test_data_exists(response):
    """Test if API returned any data"""
    data = response.json()
    if len(data) > 0:
        print(f"✅ Test Case 2 Passed: Received {len(data)} records")
    else:
        print("❌ Test Case 2 Failed: No data received")

def test_first_post_title(response):
    """Print the first post's title"""
    data = response.json()
    print("First post title:", data[0]["title"])

if __name__ == "__main__":
    response = get_posts()
    test_status_code(response)
    test_data_exists(response)
    test_first_post_title(response)