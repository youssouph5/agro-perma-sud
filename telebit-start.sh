#!/bin/bash

echo "=========================================="
echo "   AGRO PERMA SUD - Telebit Launcher     "
echo "=========================================="
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Vérifier si Telebit est installé
if ! command -v telebit &> /dev/null; then
    echo -e "${YELLOW}Telebit n'est pas installé.${NC}"
    echo ""
    read -p "Voulez-vous l'installer maintenant? (Y/n): " install_telebit
    install_telebit=${install_telebit:-Y}

    if [[ $install_telebit == "y" || $install_telebit == "Y" ]]; then
        echo -e "${BLUE}Installation de Telebit...${NC}"
        curl -fsSL https://get.telebit.io/ | bash

        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ Telebit installé avec succès!${NC}"
            echo ""
            echo -e "${YELLOW}Veuillez relancer ce script après l'installation.${NC}"
            exit 0
        else
            echo -e "${RED}✗ Erreur lors de l'installation de Telebit${NC}"
            exit 1
        fi
    else
        echo -e "${RED}Installation annulée.${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}✓ Telebit est installé${NC}"
echo ""

# Vérifier si Telebit est initialisé
if [ ! -f ~/.config/telebit/telebit.yml ]; then
    echo -e "${YELLOW}Telebit n'est pas configuré.${NC}"
    echo ""
    echo "Lançons la configuration..."
    telebit init

    if [ $? -ne 0 ]; then
        echo -e "${RED}✗ Erreur lors de la configuration${NC}"
        exit 1
    fi
fi

echo ""
echo "=========================================="
echo "Vérification des services"
echo "=========================================="

# Vérifier Nginx
if systemctl is-active --quiet nginx; then
    echo -e "${GREEN}✓ Nginx est actif${NC}"
    NGINX_RUNNING=true
else
    echo -e "${YELLOW}⚠ Nginx n'est pas actif${NC}"
    NGINX_RUNNING=false
    read -p "Voulez-vous démarrer Nginx? (Y/n): " start_nginx
    start_nginx=${start_nginx:-Y}

    if [[ $start_nginx == "y" || $start_nginx == "Y" ]]; then
        sudo systemctl start nginx
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ Nginx démarré${NC}"
            NGINX_RUNNING=true
        fi
    fi
fi

# Vérifier le backend
BACKEND_PORT=5000
if lsof -Pi :$BACKEND_PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo -e "${GREEN}✓ Backend (port $BACKEND_PORT) est actif${NC}"
else
    echo -e "${YELLOW}⚠ Backend n'est pas actif${NC}"
    echo "  Pour démarrer le backend:"
    echo "  cd backend && python run.py > backend.log 2>&1 &"
fi

# Vérifier le frontend
FRONTEND_PORT=3000
if lsof -Pi :$FRONTEND_PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo -e "${GREEN}✓ Frontend (port $FRONTEND_PORT) est actif${NC}"
else
    echo -e "${YELLOW}⚠ Frontend n'est pas actif${NC}"
    echo "  Pour démarrer le frontend:"
    echo "  cd frontend && npm run dev &"
fi

echo ""
echo "=========================================="
echo "Configuration Telebit"
echo "=========================================="

# Demander le nom de serveur
read -p "Nom de domaine souhaité (default: agro-perma-sud): " servername
servername=${servername:-agro-perma-sud}

# Demander le port à exposer
echo ""
echo "Quel port voulez-vous exposer?"
echo "  1) Port 80 (Nginx - Recommandé)"
echo "  2) Port 3000 (Frontend direct)"
echo "  3) Port 5000 (Backend direct)"
read -p "Votre choix (1-3): " port_choice

case $port_choice in
    1)
        PORT=80
        PROTOCOL="http"
        echo -e "${BLUE}Exposition via Nginx (port 80)${NC}"
        ;;
    2)
        PORT=3000
        PROTOCOL="http"
        echo -e "${BLUE}Exposition du frontend (port 3000)${NC}"
        ;;
    3)
        PORT=5000
        PROTOCOL="http"
        echo -e "${BLUE}Exposition du backend (port 5000)${NC}"
        ;;
    *)
        PORT=80
        PROTOCOL="http"
        echo -e "${YELLOW}Choix invalide, utilisation du port 80 par défaut${NC}"
        ;;
esac

echo ""
echo "=========================================="
echo "Démarrage du tunnel Telebit"
echo "=========================================="
echo ""
echo -e "${BLUE}Lancement: telebit $PROTOCOL $PORT --servername $servername${NC}"
echo ""
echo -e "${GREEN}Votre site sera accessible sur:${NC}"
echo -e "${GREEN}https://$servername.telebit.io${NC}"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter le tunnel"
echo ""
echo "=========================================="
echo ""

# Lancer Telebit
telebit $PROTOCOL $PORT --servername $servername
