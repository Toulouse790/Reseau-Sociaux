# create_script_tiktok.py

from dotenv import load_dotenv
import os
import openai
import time

# 1. Charger la clé API
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 2. Initialiser le client
client = openai.OpenAI()

# 3. ID de ton agent TikTok
assistant_id = "asst_j23vgrOETrVdsdJno9VLKGKu"

# 4. Créer un thread
thread = client.beta.threads.create()

# 5. Ajouter un message avec ton thème du jour
theme = "Paris"
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=f"Crée un script TikTok sur : {theme}"
)

# 6. Lancer le run
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant_id,
)

# 7. Attendre que le run soit terminé
while True:
    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id,
    )
    if run_status.status == "completed":
        break
    elif run_status.status == "failed":
        print("❌ Le run a échoué.")
        exit()
    time.sleep(2)

# 8. Récupérer la réponse finale
messages = client.beta.threads.messages.list(thread_id=thread.id)
final_message = messages.data[0].content[0].text.value

# 9. Afficher le résultat
print("\n🧠 Script TikTok généré :\n")
print(final_message)
