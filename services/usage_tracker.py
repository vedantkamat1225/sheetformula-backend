async def increment_usage(user_id: str):
    async with httpx.AsyncClient() as client:
        await client.patch(
            f"{BASE_URL}/collections/users/records/{user_id}",
            json={"usage_today": {"+": 1}}
        )
 