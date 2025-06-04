# services/supabase_service.py

from utils.supabase import supabase
from datetime import datetime
import uuid

async def upgrade_user_plan(email, amount, currency, transaction_id):
    # Step 1: Find user by email
    res = supabase.table("users").select("*").eq("email", email).execute()
    if not res.data:
        raise Exception("User not found")

    user = res.data[0]
    user_id = user['id']

    # Step 2: Add payment record
    supabase.table("payments").insert({
        "id": str(uuid.uuid4()),
        "user_id": user_id,
        "amount": amount,
        "currency": currency,
        "paypal_email": email,
        "transaction_id": transaction_id,
        "created_at": datetime.utcnow().isoformat()
    }).execute()

    # Step 3: (Optional) Update user role or plan field if needed
    # Example:
    # supabase.table("users").update({"plan": "pro"}).eq("id", user_id).execute()
