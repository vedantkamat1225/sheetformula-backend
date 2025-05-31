from fastapi import APIRouter, Request, HTTPException
from services.pocketbase_client import get_user
from services.usage_tracker import increment_usage
from services.openai_service import generate_formula, explain_formula

router = APIRouter()

@router.post("/formula/generate")
async def generate_formula_endpoint(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    
    # ✅ Extract and validate user from JWT
    user = await get_user(request)
    
    # ✅ Track usage
    await increment_usage(user['record']['id'])

    # ✅ Generate formula
    formula = await generate_formula(prompt)
    return {"formula": formula}


@router.post("/formula/explain")
async def explain_formula_endpoint(request: Request):
    data = await request.json()
    formula = data.get("formula")

    # ✅ Extract and validate user from JWT
    user = await get_user(request)

    # ✅ Track usage
    await increment_usage(user['record']['id'])

    # ✅ Explain formula
    explanation = await explain_formula(formula)
    return {"explanation": explanation}
