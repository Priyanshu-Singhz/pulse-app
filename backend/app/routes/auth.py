from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(body: LoginRequest):
    # validate credentials against DB
    return {"token": "placeholder"}

@router.post("/logout")
def logout():
    return {"message": "logged out"}
