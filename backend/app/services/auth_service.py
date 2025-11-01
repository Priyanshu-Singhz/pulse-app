import jwt
from datetime import datetime, timedelta
from app.models.user import User

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

def create_access_token(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=48)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

// updated 4138

// updated 8648

// updated 7645

// updated 2972

// updated 9710

// updated 7755

// updated 2370

// updated 7717

// updated 6543
