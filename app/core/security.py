from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Header, HTTPException

from app.core.config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_MINUTES



def create_token(data: dict):

    payload = data.copy()

    payload["exp"] = datetime.utcnow() + timedelta(
        minutes=TOKEN_EXPIRE_MINUTES

    )

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_token(token: str = Header(...)):

    try:

        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return token

    except JWTError:

        raise HTTPException(401, "Invalid token")
