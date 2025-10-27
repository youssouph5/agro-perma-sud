#!/bin/bash
# Script de démarrage robuste pour le développement

echo "🚀 Démarrage du serveur de développement..."

# Vérifier la syntaxe Python avant de démarrer
echo "🔍 Vérification de la syntaxe..."
python3 -m py_compile run.py app/__init__.py
if [ $? -ne 0 ]; then
    echo "❌ Erreur de syntaxe détectée. Corrigez les erreurs avant de démarrer."
    exit 1
fi

echo "✅ Syntaxe correcte"

# Activer l'environnement virtuel si disponible
if [ -d "venv" ]; then
    echo "📦 Activation de l'environnement virtuel..."
    source venv/bin/activate
fi

# Démarrer Flask
echo "🌐 Démarrage de Flask..."
export FLASK_APP=run.py
export FLASK_DEBUG=1
export PYTHONUNBUFFERED=1

python3 run.py 2>&1 | tee backend.log
