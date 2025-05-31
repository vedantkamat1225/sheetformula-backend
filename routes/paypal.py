from fastapi import APIRouter, Request
from services.pocketbase_client import upgrade_user_plan

router = APIRouter()

@router.post("/webhook")
async def paypal_webhook(request: Request):
    payload = await request.json()

    if payload.get("event_type") == "CHECKOUT.ORDER.APPROVED":
        payer_info = payload['resource']['payer']
        email = payer_info['email_address']
        await upgrade_user_plan(email)
        return {"status": "upgraded"}
    
    return {"status": "ignored"}
 