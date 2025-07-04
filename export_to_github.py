import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")  # Format : username/nom-du-repo

def upload_file_to_github(local_path, repo_path, commit_message="Ajout automatique via script"):
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(GITHUB_REPO)

        with open(local_path, "r", encoding="utf-8") as file:
            content = file.read()

        try:
            contents = repo.get_contents(repo_path)
            repo.update_file(contents.path, commit_message, content, contents.sha)
            print(f"✅ Fichier mis à jour : {repo_path}")
        except Exception:
            repo.create_file(repo_path, commit_message, content)
            print(f"✅ Fichier créé : {repo_path}")

    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    # Exemple : upload du plan contenu
    upload_file_to_github("plan_contenu.md", "plan_contenu.md", "Ajout ou mise à jour du plan contenu")
