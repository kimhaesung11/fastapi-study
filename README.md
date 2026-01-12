# fastapi-study 🚀

FastAPI + PostgreSQL + Streamlit (Docker Compose) 연동 예제 프로젝트입니다.  
Streamlit에서 입력 → FastAPI API 호출 → PostgreSQL DB 저장 → DBeaver로 확인까지 가능한 구조입니다.

---

## ✅ Features
- Docker Compose로 **API + DB** 실행
- FastAPI Swagger 문서 자동 생성
- Streamlit UI로 데이터 입력 및 API 호출
- PostgreSQL 저장 결과를 DBeaver로 확인 가능

---

## ✅ Tech Stack
- FastAPI
- PostgreSQL
- Streamlit
- Docker / Docker Compose
- DBeaver (DB 확인용)
- gunicorn (uvicorn worker)

---

## 📁 Project Structure
fastapi-study/
├── docker-compose.yml
├── Dockerfile
├── main.py
├── streamlit_app.py
├── requirements.txt
└── .gitignore

---

## 🚀 Quick Start

### 1) Clone
```bash
git clone https://github.com/kimhaesung11/fastapi-study.git
cd fastapi-study

docker compose up --build

| Service         | URL                                                      |
| --------------- | -------------------------------------------------------- |
| FastAPI Swagger | [http://localhost:8000/docs](http://localhost:8000/docs) |
| FastAPI Root    | [http://localhost:8000](http://localhost:8000)           |
| Streamlit       | [http://localhost:8501](http://localhost:8501)           |

docker-compose.yml 기준:

Host: localhost

Port: 5432

Database: study

Username: me

Password: 1234

✅ Flow (동작 구조)

Streamlit에서 입력

Streamlit → FastAPI API 호출

FastAPI → PostgreSQL 저장

DBeaver에서 DB 저장 확인
포트 충돌 시

8000 / 5432 / 8501 포트가 이미 사용 중이면 실행이 안 될 수 있습니다.
이 경우 docker-compose.yml에서 포트를 변경하세요.

DB 초기화 후 재시작
docker compose down -v
docker compose up --build

