# Configuration Flask pour le développement
FLASK_APP=run.py
FLASK_DEBUG=1

# Exclure certains fichiers du rechargement automatique
# pour éviter les rechargements inutiles
FLASK_RUN_EXTRA_FILES=
FLASK_RUN_EXCLUDE_PATTERNS=*.log,*.pyc,__pycache__,*.tmp,upload_content.py
