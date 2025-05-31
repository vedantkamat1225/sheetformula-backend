# main.py
from fastapi import FastAPI
from routes import auth, formula
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SheetFormula.ai Backend")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(formula.router, prefix="/formula", tags=["Formula"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)