from fastapi import FastAPI
from app.routes import auth, users

app = FastAPI(title="API", version="1.0.0")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
