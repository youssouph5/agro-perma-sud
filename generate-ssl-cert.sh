#!/bin/bash
# Script pour générer un certificat SSL auto-signé pour le développement local

# Créer le répertoire pour les certificats
mkdir -p ssl

# Générer le certificat auto-signé
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ssl/agro-perma-sud.key \
  -out ssl/agro-perma-sud.crt \
  -subj "/C=FR/ST=Occitanie/L=Toulouse/O=Agro Perma Sud/CN=agro-perma-sud.com" \
  -addext "subjectAltName=DNS:agro-perma-sud.com,DNS:www.agro-perma-sud.com"

echo "✓ Certificat SSL généré avec succès!"
echo "Fichiers créés:"
echo "  - ssl/agro-perma-sud.key (clé privée)"
echo "  - ssl/agro-perma-sud.crt (certificat)"
echo ""
echo "Pour utiliser ce certificat avec Nginx, copiez-le:"
echo "  sudo cp ssl/agro-perma-sud.crt /etc/ssl/certs/"
echo "  sudo cp ssl/agro-perma-sud.key /etc/ssl/private/"
echo "  sudo chmod 600 /etc/ssl/private/agro-perma-sud.key"
