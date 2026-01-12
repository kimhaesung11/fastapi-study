from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, text

app = FastAPI()

# ✅ DB 연결 (너가 만든 docker postgres 기준)
DB_URL = DB_URL = "postgresql+psycopg://me:1234@db:5432/study"
engine = create_engine(DB_URL, echo=True)


class NoteIn(BaseModel):
    content: str = Field(min_length=1, max_length=200)


@app.get("/")
def root():
    return {"message": "FastAPI is running"}


@app.get("/notes")
def list_notes():
    with engine.begin() as conn:
        rows = conn.execute(
            text("SELECT id, content, created_at FROM notes ORDER BY id DESC")
        ).mappings().all()
    return {"items": list(rows)}


@app.post("/notes")
def create_note(note: NoteIn):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO notes (content) VALUES (:c)"),
            {"c": note.content},
        )
    return {"ok": True}
