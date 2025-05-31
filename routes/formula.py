from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from services.openai_service import generate_formula_from_prompt

router = APIRouter()

class FormulaRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate_formula(req: FormulaRequest):
    try:
        formula = generate_formula_from_prompt(req.prompt)
        return {"formula": formula}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
