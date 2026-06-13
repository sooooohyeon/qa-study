# qa-study
QA 자동화 학습 기록

# QA 자동화 스터디

QA 엔지니어로 일하면서 테스트 자동화 역량을 쌓기 위해 공부한 내용을 기록하는 저장소입니다.

## 📂 구성

- `api-test/` : API 테스트 자동화 (pytest + requests)
- `web-test/` : 웹 테스트 자동화 (예정)
- `app-test/` : 앱 테스트 자동화 (예정)

## 🛠 사용 기술

- Python 3.9
- pytest
- requests

## 📌 api-test 폴더 설명

JSONPlaceholder(연습용 API)를 대상으로 작성한 API 자동화 테스트입니다.

### 테스트 항목
- GET 요청 - 정상 데이터 조회 (200)
- GET 요청 - 존재하지 않는 데이터 조회 (404)
- POST 요청 - 데이터 생성 (201)

### 실행 방법
\`\`\`
pip3 install requests pytest
python3 -m pytest test_users.py -v
\`\`\`