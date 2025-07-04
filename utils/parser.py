import re

def extraire_blocs_tiktok(texte: str) -> dict:
    """
    Extrait les blocs Hook / Déroulement / Appel à l'action à partir d'un texte brut.
    """
    hook = ""
    deroulement = ""
    cta = ""

    # Pattern simple basé sur mots-clés
    lines = texte.splitlines()
    for line in lines:
        line_clean = line.strip().lower()
        if "si je vous disais" in line_clean or "imagine" in line_clean or "vous saviez" in line_clean:
            hook += line.strip() + "\n"
        elif any(word in line_clean for word in ["comment", "dites-moi", "commentez", "abonne", "like"]):
            cta += line.strip() + "\n"
        else:
            deroulement += line.strip() + "\n"

    return {
        "hook": hook.strip(),
        "deroulement": deroulement.strip(),
        "cta": cta.strip()
    }
