# services/openai_service.py
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_formula(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Write Excel formula for: {prompt}"}]
    )
    return response["choices"][0]["message"]["content"].strip()

async def explain_formula(formula: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Explain this Excel formula: {formula}"}]
    )
    return response["choices"][0]["message"]["content"].strip()