#!/bin/bash

echo "=========================================="
echo "   AGRO PERMA SUD - LocalTunnel          "
echo "=========================================="
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "=========================================="
echo "Vérification des services"
echo "=========================================="

# Vérifier le frontend
if lsof -Pi :3000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo -e "${GREEN}✓ Frontend (port 3000) est actif${NC}"
    FRONTEND_RUNNING=true
else
    echo -e "${RED}✗ Frontend n'est pas actif${NC}"
    echo ""
    echo "Veuillez démarrer le frontend:"
    echo "  cd frontend && npm run dev"
    echo ""
    read -p "Voulez-vous continuer quand même? (y/N): " continue_anyway
    if [[ ! $continue_anyway == "y" && ! $continue_anyway == "Y" ]]; then
        exit 1
    fi
fi

# Vérifier le backend
if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo -e "${GREEN}✓ Backend (port 5000) est actif${NC}"
else
    echo -e "${YELLOW}⚠ Backend n'est pas actif${NC}"
    echo "  Démarrez-le avec: cd backend && python run.py"
fi

# Vérifier Nginx
if systemctl is-active --quiet nginx 2>/dev/null; then
    echo -e "${GREEN}✓ Nginx est actif${NC}"
else
    echo -e "${YELLOW}⚠ Nginx n'est pas actif${NC}"
fi

echo ""
echo "=========================================="
echo "Quel port voulez-vous exposer?"
echo "=========================================="
echo "  1) Port 3000 (Frontend direct) - Recommandé"
echo "  2) Port 80 (Nginx - Backend + Frontend)"
echo "  3) Port 5000 (Backend API uniquement)"
read -p "Votre choix (1-3) [1]: " port_choice
port_choice=${port_choice:-1}

case $port_choice in
    1)
        PORT=3000
        SUBDOMAIN="agro-perma-sud"
        echo -e "${BLUE}Exposition du frontend (port 3000)${NC}"
        ;;
    2)
        PORT=80
        SUBDOMAIN="agro-perma-sud"
        echo -e "${BLUE}Exposition via Nginx (port 80)${NC}"
        ;;
    3)
        PORT=5000
        SUBDOMAIN="agro-perma-sud-api"
        echo -e "${BLUE}Exposition du backend (port 5000)${NC}"
        ;;
    *)
        PORT=3000
        SUBDOMAIN="agro-perma-sud"
        echo -e "${YELLOW}Choix invalide, utilisation du port 3000${NC}"
        ;;
esac

echo ""
echo "=========================================="
echo "Démarrage de LocalTunnel"
echo "=========================================="
echo ""

# Obtenir le mot de passe du tunnel (IP publique)
echo -e "${BLUE}Récupération du mot de passe du tunnel...${NC}"
TUNNEL_PASSWORD=$(curl -s https://loca.lt/mytunnelpassword)

echo ""
echo -e "${GREEN}✓ Votre site sera accessible via:${NC}"
echo -e "${GREEN}  https://${SUBDOMAIN}.loca.lt${NC}"
echo ""
echo -e "${YELLOW}🔑 Mot de passe du tunnel (première visite):${NC}"
echo -e "${YELLOW}  ${TUNNEL_PASSWORD}${NC}"
echo ""
echo -e "${BLUE}Instructions pour les visiteurs:${NC}"
echo "  1. Allez sur https://${SUBDOMAIN}.loca.lt"
echo "  2. Entrez le mot de passe: ${TUNNEL_PASSWORD}"
echo "  3. Cliquez sur 'Submit'"
echo ""
echo -e "${YELLOW}Note:${NC}"
echo "  - Ce mot de passe est votre IP publique"
echo "  - Les visiteurs ne le verront qu'une fois tous les 7 jours"
echo "  - Partagez-le avec vos visiteurs"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter le tunnel"
echo ""
echo "=========================================="
echo ""

# Lancer LocalTunnel
npx localtunnel --port $PORT --subdomain $SUBDOMAIN
