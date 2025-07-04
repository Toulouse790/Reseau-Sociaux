from github import Github
import os

def push_to_github(file_path: str):
    token = os.getenv("GITHUB_TOKEN")
    repo_name = "Toulouse790/Reseau-So"
    commit_message = f"📤 Update automatique de {file_path}"

    g = Github(token)
    repo = g.get_repo(repo_name)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        contents = repo.get_contents(file_path)
        repo.update_file(contents.path, commit_message, content, contents.sha)
    except:
        repo.create_file(file_path, commit_message, content)
    print(f"✅ Fichier mis à jour : {file_path}")
