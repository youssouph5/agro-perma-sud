# Guide de Développement - Backend

## 🚀 Démarrage du serveur

### Méthode recommandée
```bash
./start_dev.sh
```

### Méthode manuelle
```bash
source venv/bin/activate
export FLASK_APP=run.py
export FLASK_DEBUG=1
python run.py
```

## 🛡️ Éviter les erreurs de rechargement

### ❌ Problèmes courants

**Erreur de syntaxe lors du rechargement :**
```
SyntaxError: invalid syntax
 * Restarting with stat
```

**Causes :**
1. Erreur de syntaxe dans un fichier Python
2. Caractères spéciaux mal encodés
3. Guillemets non fermés
4. Indentation incorrecte

### ✅ Solutions

#### 1. **Vérifier la syntaxe avant de sauvegarder**
```bash
# Vérifier un fichier
python3 -m py_compile app/__init__.py

# Vérifier tous les fichiers Python
find . -name "*.py" -exec python3 -m py_compile {} \;
```

#### 2. **Configurer votre éditeur**

**VSCode - settings.json :**
```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "files.encoding": "utf8"
}
```

#### 3. **Utiliser .flaskenv pour la configuration**
Le fichier `.flaskenv` contient :
- Variables d'environnement Flask
- Patterns d'exclusion pour le rechargement
- Configuration du debug

#### 4. **Fichiers à exclure du rechargement**
Ces fichiers ne doivent PAS déclencher un rechargement :
- `*.log` - fichiers de logs
- `*.pyc` - bytecode Python
- `__pycache__/` - cache Python
- `upload_content.py` - scripts utilitaires
- `*.tmp` - fichiers temporaires

## 🔍 Debugging

### Logs
Les logs sont écrits dans `backend.log` automatiquement avec le script de démarrage.

### Activer le mode verbose
```bash
export PYTHONUNBUFFERED=1
export FLASK_DEBUG=1
python run.py
```

### Désactiver le rechargement automatique
Si vous avez trop de problèmes, désactivez temporairement :
```python
# Dans run.py
app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
```

## 📝 Bonnes pratiques

### Avant chaque commit
```bash
# 1. Vérifier la syntaxe
python3 -m py_compile $(find . -name "*.py")

# 2. Formater le code
black .

# 3. Linter
pylint app/

# 4. Tests
pytest
```

### Gestion des caractères spéciaux
Toujours utiliser l'encodage UTF-8 :
```python
# En-tête de fichier
# -*- coding: utf-8 -*-

# Ou utiliser des strings brutes pour les caractères spéciaux
message = "API Agroécologie & Permaculture"  # ✅ OK
```

### Gestion des imports
```python
# ✅ Bon - imports absolus
from app.models import User
from app.services.email_service import send_email

# ❌ Éviter - imports relatifs ambigus
from ..models import User
```

## 🔧 Outils utiles

### Installation des outils de développement
```bash
pip install black pylint flake8 pytest
```

### Pre-commit hooks
Créer `.git/hooks/pre-commit` :
```bash
#!/bin/bash
python3 -m py_compile $(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')
if [ $? -ne 0 ]; then
    echo "❌ Erreur de syntaxe détectée. Commit annulé."
    exit 1
fi
```

## 📚 Ressources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Flask Best Practices](https://flask.palletsprojects.com/en/2.3.x/patterns/)

## 🆘 En cas de problème

1. Vérifiez les logs dans `backend.log`
2. Validez la syntaxe de tous les fichiers Python
3. Vérifiez l'encodage des fichiers (doit être UTF-8)
4. Redémarrez le serveur avec `./start_dev.sh`
5. Si le problème persiste, désactivez `use_reloader` temporairement
