import requests
import pytest


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


# 테스트 3: 새 유저 생성 (POST)
def test_create_user():
    payload = {
        "name": "전소현",
        "email": "sohyeon@test.com"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)
    
    assert response.status_code == 201
    assert response.json()["name"] == "전소현"
    assert response.json()["email"] == "sohyeon@test.com"


# 테스트 4: 유저 정보 수정 (PUT)
def test_update_user():
    payload = {
        "name": "전소현 수정됨",
        "email": "updated@test.com"
    }
    response = requests.put("https://jsonplaceholder.typicode.com/users/1", json=payload)
    
    assert response.status_code == 200
    assert response.json()["name"] == "전소현 수정됨"
    assert response.json()["email"] == "updated@test.com"


# 테스트 5: 유저 삭제 (DELETE)
def test_delete_user():
    response = requests.delete("https://jsonplaceholder.typicode.com/users/1")
    
    assert response.status_code == 200


# 테스트 6: 잘못된 형식의 데이터로 생성 요청 (엣지케이스)
def test_create_user_with_empty_body():
    response = requests.post("https://jsonplaceholder.typicode.com/users", json={})
    
    # JSONPlaceholder는 빈 값이어도 201을 반환 (가짜 서버 특성)
    # 실제 서버라면 400 Bad Request가 와야 정상
    print(f"상태코드: {response.status_code}")
    print(f"응답값: {response.json()}")
    
    assert response.status_code == 201
    

# 테스트 7: 응답 헤더 검증 (Content-Type이 JSON인지 확인)
def test_response_header_is_json():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    
    print(f"Content-Type: {response.headers['Content-Type']}")
    
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]


# 테스트 8: 여러 유저 ID를 한번에 검증 (파라미터화)
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_multiple_users(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    
    assert response.status_code == 200
    assert response.json()["id"] == user_id
