import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_formula_from_prompt(prompt: str) -> str:
    system_prompt = (
        "You are an expert in Excel and Google Sheets formulas. "
        "Convert user queries into working Excel/Sheets formulas."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    formula = response["choices"][0]["message"]["content"].strip()
    return formula
