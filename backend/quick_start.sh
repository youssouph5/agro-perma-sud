#!/bin/bash
# Script de démarrage rapide avec SQLite

echo "🚀 Démarrage rapide - Agroécologie & Permaculture"
echo ""

# Couleurs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Vérifier que nous sommes dans le bon dossier
if [ ! -f "run.py" ]; then
    echo -e "${RED}❌ Erreur: Exécutez ce script depuis le dossier backend${NC}"
    exit 1
fi

# Vérifier l'environnement virtuel
if [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${YELLOW}⚠️  L'environnement virtuel n'est pas activé${NC}"
    echo "Activation de l'environnement virtuel..."
    source venv/bin/activate
fi

echo -e "${GREEN}✅ Environnement virtuel activé${NC}"
echo ""

# Nettoyer les anciennes données
echo -e "${YELLOW}Étape 1: Nettoyage${NC}"
rm -f agriculture.db
rm -rf migrations
echo -e "${GREEN}✅ Nettoyage terminé${NC}"
echo ""

# Initialiser les migrations
echo -e "${YELLOW}Étape 2: Initialisation des migrations${NC}"
export FLASK_APP=run.py
flask db init
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Erreur lors de l'initialisation${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Migrations initialisées${NC}"
echo ""

# Créer la migration initiale
echo -e "${YELLOW}Étape 3: Création de la migration${NC}"
flask db migrate -m "Initial migration"
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Erreur lors de la création de la migration${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Migration créée${NC}"
echo ""

# Appliquer les migrations
echo -e "${YELLOW}Étape 4: Application des migrations${NC}"
flask db upgrade
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Erreur lors de l'application${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Base de données créée${NC}"
echo ""

# Créer les données de test
echo -e "${YELLOW}Étape 5: Création des données de test${NC}"
flask seed-db
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}⚠️  Commande seed-db non disponible${NC}"
    echo "Création manuelle d'un admin..."
    python3 << 'PYEOF'
from app import create_app, db
from app.models import User

app = create_app()
with app.app_context():
    # Vérifier si admin existe déjà
    admin = User.query.filter_by(email='admin@agriculture.com').first()
    if not admin:
        admin = User(
            email='admin@agriculture.com',
            first_name='Admin',
            last_name='Système',
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("✅ Utilisateur admin créé")
        print("   Email: admin@agriculture.com")
        print("   Mot de passe: admin123")
    else:
        print("✅ Admin déjà existant")
PYEOF
fi
echo -e "${GREEN}✅ Données de test créées${NC}"
echo ""

# Résumé
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}🎉 Installation terminée avec succès !${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "📝 Informations:"
echo "   - Base de données: SQLite (agriculture.db)"
echo "   - Admin: admin@agriculture.com / admin123"
echo ""
echo "🚀 Pour démarrer le serveur:"
echo "   python run.py"
echo ""
echo "🌐 URLs:"
echo "   - Backend API: http://localhost:5000"
echo "   - Health check: http://localhost:5000/health"
echo ""
