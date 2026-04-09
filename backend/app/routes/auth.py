from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(body: LoginRequest):
    # TODO: validate credentials
    return {"token": "placeholder"}

@router.post("/logout")
def logout():
    return {"message": "logged out"}
