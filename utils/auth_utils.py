# utils/auth_utils.py
from fastapi import Request, HTTPException
from services.jwt import verify_token

async def get_current_user(request: Request):
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Missing token")

    token = auth.split(" ")[1]
    decoded = verify_token(token)
    if not decoded:
        raise HTTPException(status_code=403, detail="Invalid token")

    return decoded
