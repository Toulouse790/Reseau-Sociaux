from agents.veille import get_trending_topics
from agents.strategie import generate_content_strategy
from agents.tiktok import create_tiktok_script
from datetime import datetime

# 1. Récupérer une tendance TikTok
trends = get_trending_topics()
trend = trends[0]  # Tu peux boucler plus tard

# 2. Générer une stratégie de contenu
strategie = generate_content_strategy(trend)

# 3. Générer un script TikTok
script = create_tiktok_script(strategie)

# 4. Générer un fichier Markdown
md_content = f"""# 📈 Plan de contenu TikTok généré par IA

## 🔥 Tendance détectée
{trend}

## 🧠 Stratégie proposée
{strategie}

## 🎬 Script TikTok
{script}

---

*Généré automatiquement le {datetime.now().strftime("%d/%m/%Y à %H:%M")}*
"""

with open("plan_contenu.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print("✅ plan_contenu.md généré avec succès.")
