from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(request: LoginRequest):
    if request.username == "testuser" and request.password == "secret123":
        return {"message": "Login successful", "username": request.username}
    raise HTTPException(status_code=401, detail="Invalid credentials")