# fastapi-study 🚀

FastAPI + PostgreSQL + Streamlit을 **Docker Compose**로 함께 실행하는 예제입니다.  
Streamlit 입력 → FastAPI API 호출 → PostgreSQL 저장 → DBeaver로 확인까지 가능한 구조입니다.

---

## ✅ Tech Stack
- FastAPI
- PostgreSQL
- Streamlit
- Docker / Docker Compose
- gunicorn (uvicorn worker)
- DBeaver (DB 확인)

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

## 🚀 Run (Docker Compose)
```bash
docker compose up --build
| Service         | URL                                                      |
| --------------- | -------------------------------------------------------- |
| FastAPI Swagger | [http://localhost:8000/docs](http://localhost:8000/docs) |
| Streamlit       | [http://localhost:8501](http://localhost:8501)           |

🗄️ PostgreSQL (DBeaver)

Host: localhost

Port: 5432

Database: study

Username: me

Password: 1234

✅ Flow

Streamlit에서 입력

Streamlit → FastAPI 호출 (API_BASE_URL)

FastAPI → PostgreSQL 저장

DBeaver에서 저장 확인

🧹 Reset (DB 포함 초기화)
docker compose down -v
docker compose up --build
FastAPI: http://localhost:8000/docs

Streamlit: http://localhost:8501
