# services/jwt.py
from jose import jwt, JWTError
from datetime import datetime, timedelta
import os

SECRET_KEY = os.getenv("JWT_SECRET") or "secret"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta = timedelta(days=7)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None