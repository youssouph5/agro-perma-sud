#!/bin/bash

echo "=========================================="
echo "   AGRO PERMA SUD - Helper Déploiement   "
echo "=========================================="
echo ""

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Vérifier si Git est initialisé
if [ ! -d .git ]; then
    echo -e "${YELLOW}Git n'est pas initialisé. Initialisation...${NC}"
    git init
    git branch -M main
    echo -e "${GREEN}✓ Git initialisé${NC}"
else
    echo -e "${GREEN}✓ Git déjà initialisé${NC}"
fi

echo ""
echo "=========================================="
echo "Configuration Git"
echo "=========================================="

# Demander le nom d'utilisateur GitHub si pas configuré
if [ -z "$(git config user.name)" ]; then
    read -p "Entrez votre nom pour Git: " git_name
    git config user.name "$git_name"
fi

if [ -z "$(git config user.email)" ]; then
    read -p "Entrez votre email pour Git: " git_email
    git config user.email "$git_email"
fi

echo -e "${GREEN}✓ Configuration Git terminée${NC}"
echo "  Nom: $(git config user.name)"
echo "  Email: $(git config user.email)"

echo ""
echo "=========================================="
echo "Préparation du commit"
echo "=========================================="

# Ajouter tous les fichiers
git add .

# Créer le commit
read -p "Message de commit (ou appuyez sur Entrée pour 'Initial commit'): " commit_msg
commit_msg=${commit_msg:-"Initial commit - Agro Perma Sud"}

git commit -m "$commit_msg"

echo -e "${GREEN}✓ Commit créé${NC}"

echo ""
echo "=========================================="
echo "Configuration du repository GitHub"
echo "=========================================="

# Vérifier si un remote existe déjà
if git remote | grep -q origin; then
    echo -e "${YELLOW}Remote 'origin' existe déjà:${NC}"
    git remote -v
    read -p "Voulez-vous le remplacer? (y/N): " replace_remote
    if [[ $replace_remote == "y" || $replace_remote == "Y" ]]; then
        git remote remove origin
        echo -e "${GREEN}✓ Remote supprimé${NC}"
    fi
fi

# Ajouter le remote si nécessaire
if ! git remote | grep -q origin; then
    echo ""
    echo "Créez d'abord un repository sur GitHub:"
    echo "  1. Allez sur https://github.com/new"
    echo "  2. Nom: agro-perma-sud"
    echo "  3. NE PAS cocher 'Initialize with README'"
    echo "  4. Cliquez 'Create repository'"
    echo ""
    read -p "Entrez votre nom d'utilisateur GitHub: " github_user

    git remote add origin "https://github.com/$github_user/agro-perma-sud.git"
    echo -e "${GREEN}✓ Remote ajouté${NC}"
fi

echo ""
echo "=========================================="
echo "Push vers GitHub"
echo "=========================================="

read -p "Voulez-vous pousser le code maintenant? (Y/n): " do_push
do_push=${do_push:-Y}

if [[ $do_push == "y" || $do_push == "Y" ]]; then
    echo "Pushing to GitHub..."
    git push -u origin main

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Code poussé avec succès!${NC}"
    else
        echo -e "${YELLOW}⚠ Erreur lors du push. Vérifiez vos identifiants GitHub.${NC}"
        echo "Si vous utilisez 2FA, créez un Personal Access Token:"
        echo "  https://github.com/settings/tokens"
    fi
fi

echo ""
echo "=========================================="
echo "Prochaines étapes"
echo "=========================================="
echo ""
echo -e "${BLUE}1. Allez sur https://railway.app${NC}"
echo -e "${BLUE}2. Connectez-vous avec GitHub${NC}"
echo -e "${BLUE}3. Cliquez 'New Project' > 'Deploy from GitHub repo'${NC}"
echo -e "${BLUE}4. Sélectionnez votre repository 'agro-perma-sud'${NC}"
echo ""
echo -e "${GREEN}📖 Guide détaillé: DEPLOIEMENT-RAILWAY-GUIDE.md${NC}"
echo ""
echo "=========================================="
echo "   Bonne chance avec votre déploiement!   "
echo "=========================================="
