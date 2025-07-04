import os
import time
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# 🔐 Chargement des variables d'environnement (.env)
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Initialisation client OpenAI
client = OpenAI(api_key=api_key)

# 🧠 ID de ton assistant IA
assistant_id = "asst_j23vgrOETrVdsdJno9VLKGKu"

# 🔄 Création d'un thread
thread = client.beta.threads.create()

# 💬 Envoi d'un message à l'assistant
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Génère-moi un contenu viral sur TikTok dans la niche humour français, format court 20-30s"
)

# ▶️ Lancement du run
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant_id,
)

# ⏳ Boucle d'attente jusqu'à réponse complète
while True:
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    if run_status.status == "completed":
        break
    time.sleep(1)

# 📥 Récupération de la dernière réponse
messages = client.beta.threads.messages.list(thread_id=thread.id)
last_message = messages.data[0]
print("\n🧠 Assistant a répondu :\n")
print(last_message.content[0].text.value)

# Simulons des parties pour générer un .md
hook_response = "Et si je vous disais qu’après 10 ans de français, je viens de découvrir LA vérité sur Paris ?"
deroulement_response = "Je pensais que la Tour Eiffel était une galerie marchande... Je cherchais l’étage des macarons à l'intérieur !"
cta_response = "Dites-moi que je ne suis pas seul ! Commentez vos meilleures confessions françaises !"

# 📝 Contenu markdown
md_content = f"""# Plan de Contenu TikTok - Généré par IA

## 🎯 Hook (Accroche)

> {hook_response}

## 📖 Déroulement Narratif

> {deroulement_response}

## 📢 Appel à l’Action

> {cta_response}

---

*Fichier généré automatiquement le {datetime.now().strftime("%d %B %Y à %Hh%M")}*
"""

# 💾 Sauvegarde dans un fichier .md
with open("plan_contenu.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print("✅ Fichier 'plan_contenu.md' généré avec succès.")
