from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, formula, payments
from routes import paypal

app = FastAPI(title="SheetFormula.ai Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(formula.router, prefix="/formula", tags=["Formula"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])

app.include_router(paypal.router, prefix="/paypal", tags=["PayPal"])