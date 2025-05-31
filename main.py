from fastapi import FastAPI
from routes import auth, formula, paypal

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(formula.router, prefix="/formula")
app.include_router(paypal.router, prefix="/paypal")
