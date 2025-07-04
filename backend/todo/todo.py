# backend/todo/app/todo.py

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, Todo as TodoModel

router = APIRouter()

class TodoCreate(BaseModel):
    title: str

class TodoResponse(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True

# DB 세션 종속성

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/todos/", response_model=list[TodoResponse])
def get_todos():
    db: Session = next(get_db())
    return db.query(TodoModel).all()

@router.post("/todos/", response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    db: Session = next(get_db())
    new_todo = TodoModel(title=todo.title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo