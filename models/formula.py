# models/formula.py
from pydantic import BaseModel

class FormulaRequest(BaseModel):
    prompt: str

class ExplainRequest(BaseModel):
    formula: str