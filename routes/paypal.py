# routes/paypal.py

from fastapi import APIRouter, Request
from services.supabase_service import upgrade_user_plan

router = APIRouter()

@router.post("/webhook")
async def paypal_webhook(request: Request):
    payload = await request.json()

    if payload.get("event_type") == "CHECKOUT.ORDER.APPROVED":
        payer_info = payload['resource']['payer']
        email = payer_info['email_address']
        amount = payload['resource']['purchase_units'][0]['amount']['value']
        currency = payload['resource']['purchase_units'][0]['amount']['currency_code']
        transaction_id = payload['resource']['id']

        await upgrade_user_plan(email, amount, currency, transaction_id)
        return {"status": "upgraded"}

    return {"status": "ignored"}
