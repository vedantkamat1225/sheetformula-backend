from services.usage_tracker import increment_usage
from services.openai_service import generate_formula, explain_formula
from fastapi import APIRouter, Request
from utils.auth import get_user

router = APIRouter()

@router.post("/formula/generate")
async def generate_formula_endpoint(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    user = await get_user(request)

    await increment_usage(user['record']['id'], action="generate")
    formula = await generate_formula(prompt)
    return {"formula": formula}


@router.post("/formula/explain")
async def explain_formula_endpoint(request: Request):
    data = await request.json()
    formula = data.get("formula")

    user = await get_user(request)

    await increment_usage(user['record']['id'], action="explain")
    explanation = await explain_formula(formula)
    return {"explanation": explanation}
