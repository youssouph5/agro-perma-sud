# 🌱 Plateforme Agroécologie & Permaculture

Plateforme web complète dédiée à l'agriculture durable et à la permaculture. Ce projet permet de promouvoir les pratiques agricoles modernes respectueuses de l'environnement, de partager des expériences, d'organiser des formations et de développer une communauté d'agriculteurs éco-responsables.

## 📋 Vue d'ensemble

- **Version** : 1.0
- **Date** : 16 Septembre 2025
- **Statut** : En développement
- **Budget estimé** : 24 900 - 38 100 €
- **Délai de réalisation** : 14 semaines

## 🎯 Objectifs principaux

1. **Éducatif** : Diffusion des pratiques de permaculture
2. **Commercial** : Développement d'une activité viable
3. **Communautaire** : Constitution d'un réseau d'agriculteurs
4. **Territorial** : Rayonnement local, régional et international

## 🏗️ Architecture

### Backend (Flask + Python)

- **Framework** : Flask 2.3.3
- **Base de données** : PostgreSQL 13
- **Cache** : Redis 6
- **API** : RESTful avec Flask-RESTful
- **Authentification** : JWT (Flask-JWT-Extended)
- **Paiements** : Stripe
- **Email** : Flask-Mail
- **Stockage** : AWS S3 / Google Cloud Storage

### Frontend (React + TypeScript)

- **Framework** : React 18.2 + TypeScript
- **Build** : Vite 5
- **Styling** : Tailwind CSS 3.3 (thème inspiré ANCAR)
- **Routing** : React Router v6
- **State** : Zustand + React Query
- **Animations** : Framer Motion
- **Forms** : React Hook Form + Zod

## 📁 Structure du projet

```
AgriCulture-Permaculture/
├── backend/                    # API Flask
│   ├── app/
│   │   ├── models/            # Modèles de données
│   │   ├── api/               # Routes API
│   │   ├── services/          # Services métier
│   │   ├── utils/             # Utilitaires
│   │   └── templates/         # Templates email
│   ├── deployment/            # Docker & Nginx
│   ├── config.py
│   ├── requirements.txt
│   └── run.py
│
├── frontend/                   # Interface React
│   ├── src/
│   │   ├── components/        # Composants réutilisables
│   │   ├── pages/             # Pages de l'application
│   │   ├── services/          # Services API
│   │   ├── hooks/             # Custom hooks
│   │   └── styles/            # Styles globaux
│   ├── package.json
│   └── vite.config.ts
│
└── README.md                   # Ce fichier
```

## 🚀 Installation et démarrage

### Prérequis

- Python 3.11+
- Node.js 18+
- PostgreSQL 13+
- Redis 6+

### 1. Backend

```bash
cd backend

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos configurations

# Initialiser la base de données
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
flask init-db
flask seed-db

# Démarrer le serveur
python run.py
```

Le backend sera accessible sur `http://localhost:5000`

### 2. Frontend

```bash
cd frontend

# Installer les dépendances
npm install

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos configurations

# Démarrer le serveur de développement
npm run dev
```

Le frontend sera accessible sur `http://localhost:3000`

### 3. Déploiement avec Docker

```bash
cd backend/deployment
docker-compose up -d
```

## 📚 Fonctionnalités

### 1. Gestion des Projets/Réalisations
- ✅ CRUD complet
- ✅ Galerie photos/vidéos
- ✅ Statuts de projet
- ✅ Filtrage et recherche
- ✅ Projets en vedette

### 2. Système de Formations
- ✅ Catalogue de formations
- ✅ Niveaux (débutant, intermédiaire, expert)
- ✅ Sessions programmées
- ✅ Gestion des inscriptions
- ✅ Supports pédagogiques
- ✅ Système de certification

### 3. Visites de Terrain
- ✅ Types de visites configurables
- ✅ Calendrier de réservation
- ✅ Gestion des participants
- ✅ Confirmations automatiques

### 4. Newsletter et CRM
- ✅ Inscription newsletter
- ✅ Segmentation de l'audience
- ✅ Campagnes d'emailing
- ✅ Statistiques d'engagement
- ✅ Intégration Mailchimp

### 5. Système de Paiement
- ✅ Intégration Stripe
- ✅ Paiements sécurisés
- ✅ Gestion des remboursements
- ✅ Génération de factures

### 6. Gestion des Médias
- ✅ Upload optimisé
- ✅ Stockage S3/local
- ✅ Compression automatique
- ✅ Watermarking
- ✅ Galeries interactives

## 🎨 Design

Le design est inspiré du modèle **ANCAR** (Agence Nationale de Conseil Agricole et Rural du Sénégal) pour un aspect professionnel et institutionnel.

### Palette de couleurs
- **Vert principal** : #2E7D32
- **Vert secondaire** : #4CAF50
- **Terre/Beige** : #8D6E63
- **Gris charbon** : #2C2C2C

### Typographie
- **Headers** : Roboto, Montserrat
- **Corps** : Open Sans, Source Sans Pro

## 🔐 Sécurité

- ✅ Authentification JWT
- ✅ Hashage bcrypt des mots de passe
- ✅ CORS configuré
- ✅ Validation des entrées
- ✅ Protection CSRF
- ✅ HTTPS en production
- ✅ Sauvegardes automatiques

## 📊 KPI et Métriques

### Techniques
- Temps de chargement < 3s
- Disponibilité > 99,5%
- Score SEO > 80/100

### Business
- 200 visites / an
- 120 sessions de formation / an
- 2 000 contacts newsletter
- 250 000 € de CA / an

## 🧪 Tests

### Backend
```bash
cd backend
pytest
pytest --cov=app tests/
```

### Frontend
```bash
cd frontend
npm run test
```

## 📦 Déploiement

### Backend (Production)

```bash
# Build Docker
docker build -t agriculture-backend .

# Avec docker-compose
docker-compose -f deployment/docker-compose.yml up -d
```

### Frontend (Production)

```bash
cd frontend
npm run build

# Déployer le dossier dist/ sur :
# - Vercel
# - Netlify
# - GitHub Pages
# - Serveur Nginx
```

## 📖 Documentation

- [Documentation Backend](backend/README.md)
- [Documentation Frontend](frontend/README.md)
- [Documentation API](backend/docs/api_documentation.md) *(à créer)*
- [Manuel Utilisateur](backend/docs/user_manual.md) *(à créer)*

## 🛠️ Stack Technique Complète

### Backend
- Flask 2.3.3
- PostgreSQL 13
- Redis 6
- SQLAlchemy
- Marshmallow
- Stripe SDK
- Boto3 (AWS)
- Gunicorn
- Nginx

### Frontend
- React 18.2
- TypeScript 5.2
- Vite 5
- Tailwind CSS 3.3
- React Router v6
- Zustand
- React Query
- Axios
- Framer Motion
- React Hook Form
- Zod

### DevOps
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- PostgreSQL (base de données)
- Redis (cache)
- Nginx (reverse proxy)
- Let's Encrypt (SSL)

## 🤝 Contribution

Ce projet est en développement interne. Pour toute question ou suggestion :

**Email** : contact@agriculture-permaculture.sn
**Téléphone** : +221778161138

Propriétaire - Usage interne
© 2025 Agroécologie & Permaculture. Tous droits réservés.

## 🗺️ Roadmap

### Phase 1 - MVP (3 mois)
- ✅ Backend API complet
- ✅ Frontend avec pages principales
- ✅ Système de réservation de base
- ✅ Catalogue formations

### Phase 2 - Enrichissement (6 mois)
- 🔄 Module e-learning
- 🔄 Application mobile (React Native/Flutter)
- 🔄 Système de parrainage
- 🔄 Marketplace producteurs

### Phase 3 - Optimisation (12 mois)
- 📅 Intelligence artificielle
- 📅 API publique pour partenaires
- 📅 Expansion géographique
- 📅 Intégration IoT

## 🎯 Vision

Devenir la plateforme de référence francophone pour l'agriculture durable et la permaculture, en offrant un écosystème complet de formation, d'accompagnement et de partage d'expériences.

---

**Fait avec ❤️ pour une agriculture durable**
