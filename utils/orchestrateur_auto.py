import os
from dotenv import load_dotenv
from agents.veille import get_trending_topics
from agents.strategie import generate_content_strategy
from agents.tiktok import create_tiktok_script
from utils.export_to_github import push_to_github
from datetime import datetime

# Charger les variables d’environnement
load_dotenv()

# 1️⃣ - Étape 1 : Lancer l’agent de veille
tendances = get_trending_topics()
tendance_selectionnee = tendances[0] if tendances else "Impossible de détecter une tendance."

# 2️⃣ - Étape 2 : Lancer l’agent stratégie
strategie = generate_content_strategy(tendance_selectionnee)

# 3️⃣ - Étape 3 : Lancer l’agent TikTok
script_tiktok = create_tiktok_script(tendance_selectionnee)

# 4️⃣ - Générer le fichier Markdown
markdown = f"""# 📈 Plan de contenu TikTok généré par IA

## 🔥 Tendance détectée
{tendance_selectionnee}

## 🧠 Stratégie proposée
{strategie}

## 🎬 Script TikTok
{script_tiktok}

---

*Généré automatiquement le {datetime.now().strftime('%d/%m/%Y à %H:%M')}*
"""

with open("plan_contenu.md", "w", encoding="utf-8") as f:
    f.write(markdown)

print("✅ Fichier 'plan_contenu.md' généré avec succès.")

# 5️⃣ - Push automatique vers GitHub
push_to_github("plan_contenu.md")
