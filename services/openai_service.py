import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_formula(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Convert to Excel formula: {prompt}"}],
        temperature=0.2
    )
    return response['choices'][0]['message']['content'].strip()

async def explain_formula(formula: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Explain this Excel formula: {formula}"}],
        temperature=0.2
    )
    return response['choices'][0]['message']['content'].strip()
 