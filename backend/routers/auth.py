from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# 로그인 요청 스키마
class LoginRequest(BaseModel):
    username: str
    password: str

# 임시 유저 (테스트용
fake_user = {
    "username": "testuser",
    "password": "secret123"
}

@router.post("/login")
def login(request: LoginRequest):
    if request.username != fake_user["username"] or request.password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "message": "Login successful",
        "username": request.username
    }

