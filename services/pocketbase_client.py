# services/pocketbase_client.py

import os
import httpx

BASE_URL = os.getenv("POCKETBASE_URL")

async def upgrade_user_plan(email: str):
    async with httpx.AsyncClient() as client:
        # Get user record by email
        res = await client.get(f"{BASE_URL}/collections/users/records?filter=email='{email}'")
        res.raise_for_status()

        user = res.json()['items'][0]
        user_id = user['id']

        # Patch user plan
        await client.patch(
            f"{BASE_URL}/collections/users/records/{user_id}",
            json={"plan": "pro"}
        )

async def verify_token(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_URL}/collections/users/auth-refresh", headers=headers)
        if res.status_code != 200:
            return None
        return res.json()

async def increment_usage(user_id: str):
    async with httpx.AsyncClient() as client:
        await client.patch(
            f"{BASE_URL}/collections/users/records/{user_id}",
            json={"usage_today": {"+": 1}}
        )








from fastapi import Request, HTTPException

async def get_user(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    
    user = await verify_token(token)
    if not user:
        raise HTTPException(status_code=403, detail="Invalid or expired token")
    
    return user
