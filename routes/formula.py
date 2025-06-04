# routes/formula.py
from fastapi import APIRouter, Request
from models.formula import FormulaRequest, ExplainRequest
from services.openai_service import generate_formula, explain_formula
from utils.auth_utils import get_current_user
from utils.supabase_client import supabase
from datetime import date

router = APIRouter()

@router.post("/generate")
async def generate(req: Request, body: FormulaRequest):
    user = await get_current_user(req)
    user_id = user["sub"]

    # track usage
    today = date.today()
    res = supabase.table("api_usage").select("*").eq("user_id", user_id).eq("date", today).execute()
    if res.data:
        row = res.data[0]
        supabase.table("api_usage").update({"formula_generated": row["formula_generated"] + 1}).eq("id", row["id"]).execute()
    else:
        supabase.table("api_usage").insert({"user_id": user_id, "formula_generated": 1, "formula_explained": 0}).execute()

    formula = await generate_formula(body.prompt)
    return {"formula": formula}


@router.post("/explain")
async def explain(req: Request, body: ExplainRequest):
    user = await get_current_user(req)
    user_id = user["sub"]

    # track usage
    today = date.today()
    res = supabase.table("api_usage").select("*").eq("user_id", user_id).eq("date", today).execute()
    if res.data:
        row = res.data[0]
        supabase.table("api_usage").update({"formula_explained": row["formula_explained"] + 1}).eq("id", row["id"]).execute()
    else:
        supabase.table("api_usage").insert({"user_id": user_id, "formula_generated": 0, "formula_explained": 1}).execute()

    explanation = await explain_formula(body.formula)
    return {"explanation": explanation}