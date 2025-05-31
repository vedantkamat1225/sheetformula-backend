from fastapi import APIRouter, Request, Depends, HTTPException
from services.openai_service import generate_formula, explain_formula
from services.pocketbase_client import verify_token, increment_usage

router = APIRouter()

async def get_user(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401)
    user = await verify_token(token)
    if not user:
        raise HTTPException(status_code=403)
    return user

@router.post("/generate")
async def generate(data: dict, request: Request, user=Depends(get_user)):
    await increment_usage(user['record']['id'])
    result = await generate_formula(data['prompt'])
    return {"formula": result}

@router.post("/explain")
async def explain(data: dict, request: Request, user=Depends(get_user)):
    await increment_usage(user['record']['id'])
    result = await explain_formula(data['formula'])
    return {"explanation": result}
 