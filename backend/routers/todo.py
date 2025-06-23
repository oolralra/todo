from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    redirect_slashes=False  # 추가
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.TodoRead])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@router.post("/", response_model=schemas.TodoRead)
def add_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)
