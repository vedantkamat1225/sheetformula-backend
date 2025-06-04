# routes/auth.py
from fastapi import APIRouter, HTTPException, Request
from models.user import UserCreate, UserLogin
from utils.supabase import supabase
from services.hash import hash_password, verify_password
from services.jwt import create_access_token

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate):
    existing = supabase.table("users").select("*").eq("email", user.email).execute()
    if existing.data:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pw = hash_password(user.password)
    result = supabase.table("users").insert({"email": user.email, "password_hash": hashed_pw}).execute()
    user_id = result.data[0]["id"]
    token = create_access_token({"sub": user_id})
    return {"access_token": token, "user_id": user_id}


@router.post("/login")
async def login(user: UserLogin):
    result = supabase.table("users").select("*").eq("email", user.email).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = result.data[0]
    if not verify_password(user.password, user_data["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user_data["id"]})
    return {"access_token": token, "user_id": user_data["id"]}
