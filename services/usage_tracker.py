from datetime import date
from utils.supabase import supabase

async def increment_usage(user_id: str, action: str = "generate"):
    today = str(date.today())
    
    # Check if today's record exists
    res = supabase.table("api_usage")\
        .select("*")\
        .eq("user_id", user_id)\
        .eq("date", today)\
        .execute()

    if res.data and len(res.data) > 0:
        row = res.data[0]
        field = "formula_generated" if action == "generate" else "formula_explained"
        updated_value = row[field] + 1

        supabase.table("api_usage")\
            .update({field: updated_value})\
            .eq("id", row["id"])\
            .execute()
    else:
        supabase.table("api_usage").insert({
            "user_id": user_id,
            "formula_generated": 1 if action == "generate" else 0,
            "formula_explained": 1 if action == "explain" else 0,
            "date": today
        }).execute()
