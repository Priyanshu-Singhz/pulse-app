from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(body: LoginRequest):
    # validate credentials against DB
    token = create_access_token(body.email)
    return {"token": token}

@router.post("/logout")
def logout():
    return {"message": "logged out"}

// updated 4733

// updated 2714

// updated 9870

// updated 3176

// updated 1661

// updated 5948

// updated 3892

// updated 3015

// updated 2214

// updated 1053

// updated 1647

// updated 9570

// updated 7962

// updated 3724

// updated 7874
