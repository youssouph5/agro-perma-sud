#!/bin/bash
# Script de configuration de la base de données PostgreSQL

echo "🗄️  Configuration de PostgreSQL pour Agroécologie & Permaculture"
echo ""

# Couleurs pour l'affichage
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Variables
DB_NAME="agriculture_db"
DB_USER="agriculture_user"
DB_PASS="agriculture_pass123"

echo -e "${YELLOW}Étape 1: Vérification de PostgreSQL${NC}"
if ! command -v psql &> /dev/null; then
    echo -e "${RED}❌ PostgreSQL n'est pas installé${NC}"
    echo "Installez PostgreSQL avec: sudo apt install postgresql"
    exit 1
fi
echo -e "${GREEN}✅ PostgreSQL est installé${NC}"

echo ""
echo -e "${YELLOW}Étape 2: Création de la base de données${NC}"
echo "Vous allez devoir entrer votre mot de passe sudo pour exécuter les commandes PostgreSQL"

# Créer l'utilisateur et la base de données
sudo -u postgres psql << EOF
-- Supprimer l'utilisateur et la base s'ils existent déjà
DROP DATABASE IF EXISTS $DB_NAME;
DROP USER IF EXISTS $DB_USER;

-- Créer le nouvel utilisateur
CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';

-- Créer la base de données
CREATE DATABASE $DB_NAME OWNER $DB_USER;

-- Donner tous les privilèges
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;

-- Afficher le résultat
\l $DB_NAME
EOF

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Base de données créée avec succès${NC}"
    echo ""
    echo "📝 Informations de connexion:"
    echo "   - Base de données: $DB_NAME"
    echo "   - Utilisateur: $DB_USER"
    echo "   - Mot de passe: $DB_PASS"
    echo "   - URL: postgresql://$DB_USER:$DB_PASS@localhost:5432/$DB_NAME"
else
    echo -e "${RED}❌ Erreur lors de la création de la base de données${NC}"
    exit 1
fi

echo ""
echo -e "${YELLOW}Étape 3: Test de connexion${NC}"
PGPASSWORD=$DB_PASS psql -U $DB_USER -d $DB_NAME -h localhost -c "SELECT version();" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Connexion à la base de données réussie${NC}"
else
    echo -e "${RED}❌ Impossible de se connecter à la base de données${NC}"
    echo "Vérifiez le fichier /etc/postgresql/*/main/pg_hba.conf"
    exit 1
fi

echo ""
echo -e "${GREEN}🎉 Configuration terminée !${NC}"
echo ""
echo "Prochaines étapes:"
echo "1. Activer l'environnement virtuel: source venv/bin/activate"
echo "2. Initialiser les migrations: flask db upgrade"
echo "3. Créer les données de test: flask seed-db"
echo "4. Lancer le serveur: python run.py"