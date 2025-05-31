# main.py
from fastapi import FastAPI
from routes import auth, formula

app = FastAPI(title="SheetFormula.ai Backend")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(formula.router, prefix="/formula", tags=["Formula"])

