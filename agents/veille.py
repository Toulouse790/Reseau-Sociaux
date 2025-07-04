from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_trending_topics():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Tu es un agent de veille. Donne-moi une tendance TikTok virale aujourd'hui aux USA."},
            {"role": "user", "content": "Donne-moi 3 idées très virales."}
        ]
    )
    raw = response.choices[0].message.content.strip()
    return [line.strip("- ").strip() for line in raw.split("\n") if line.strip()]
