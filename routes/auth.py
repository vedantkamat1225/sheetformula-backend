from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.post("/login")
async def login(data: dict):
    email = data.get("email")
    password = data.get("password")

    async with httpx.AsyncClient() as client:
        res = await client.post(f"{BASE_URL}/collections/users/auth-with-password", json={
            "identity": email,
            "password": password
        })
        if res.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return res.json()
