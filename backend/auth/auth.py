# backend/auth/app/auth.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

fake_user = {
    "username": "testuser",
    "password": "secret123"
}

@router.post("/login")
def login(request: LoginRequest):
    if request.username != fake_user["username"] or request.password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "access_token": "test-token",
        "token_type": "bearer"
    }