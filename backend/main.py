from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import todo  # ← 이게 반드시 있어야 함
from database import Base, engine
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo.router, tags=["todos"])

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

