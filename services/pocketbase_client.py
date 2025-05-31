import httpx
import os

BASE_URL = "http://127.0.0.1:8090/api"
HEADERS = {"Content-Type": "application/json"}

async def verify_token(token: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_URL}/collections/users/auth-refresh", headers={"Authorization": f"Bearer {token}"})
        return res.json() if res.status_code == 200 else None

async def get_user_by_id(user_id: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_URL}/collections/users/records/{user_id}")
        return res.json()

async def increment_usage(user_id: str):
    async with httpx.AsyncClient() as client:
        await client.patch(f"{BASE_URL}/collections/users/records/{user_id}", json={"usage_today": {"+": 1}})
 