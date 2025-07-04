from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_tiktok_script(brief):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Tu es un créateur de contenu TikTok. Rédige un script viral pour une vidéo de 60 secondes max."},
            {"role": "user", "content": f"Brief : {brief}"}
        ]
    )
    return response.choices[0].message.content.strip()
