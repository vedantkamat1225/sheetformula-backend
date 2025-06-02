from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.post("/signup")
def signup(user: SignupRequest):
    result = supabase.auth.sign_up(
        {
            "email": user.email,
            "password": user.password
        }
    )
    if result.get("error"):
        raise HTTPException(status_code=400, detail=result["error"]["message"])
    return {"message": "Signup successful", "data": result["user"]}


@router.post("/login")
def login(user: LoginRequest):
    result = supabase.auth.sign_in_with_password(
        {
            "email": user.email,
            "password": user.password
        }
    )
    if result.get("error"):
        raise HTTPException(status_code=400, detail=result["error"]["message"])
    return {
        "access_token": result["session"]["access_token"],
        "user": result["user"]
    }

