from fastapi import FastAPI
from todo import router  # todo.py에서 만든 router를 import

app = FastAPI()
app.include_router(router)