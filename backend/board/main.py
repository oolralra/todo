from fastapi import FastAPI
from board import router  # board.py에서 만든 router를 import

app = FastAPI()
app.include_router(router)