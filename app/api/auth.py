from fastapi import APIRouter, HTTPException
from app.core.security import create_token

router = APIRouter()


@router.post("/login")
def login(data: dict):

    if data.get("username") == "admin" and data.get("password") == "admin":

        token = create_token({"user": "admin"})

        return {"access_token": token}

    raise HTTPException(401, "Invalid credentials")
