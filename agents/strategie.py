from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content_strategy(trend):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Tu es un agent stratégie. Tu reçois une tendance TikTok et tu proposes le format idéal de contenu à publier."},
            {"role": "user", "content": f"Tendance détectée : {trend}"}
        ]
    )
    return response.choices[0].message.content.strip()
