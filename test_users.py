import requests

# 테스트 1: 정상 유저 조회 (200)
def test_get_user_success():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Leanne Graham"

# 테스트 2: 없는 유저 조회 (404)
def test_get_user_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
    
    assert response.status_code == 404