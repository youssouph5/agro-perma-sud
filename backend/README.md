# Backend - Plateforme Agroécologie & Permaculture

Backend Flask pour la plateforme web d'agriculture durable et permaculture.

## Architecture

- **Framework**: Flask 2.3.3
- **Base de données**: PostgreSQL
- **Cache**: Redis
- **API**: RESTful avec Flask-RESTful
- **Authentification**: JWT (Flask-JWT-Extended)

## Structure du projet

```
backend/
├── app/
│   ├── __init__.py           # Factory Flask
│   ├── models/               # Modèles de données
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── training.py
│   │   ├── visit.py
│   │   ├── media.py
│   │   └── newsletter.py
│   ├── api/                  # Routes API
│   │   ├── auth.py
│   │   ├── projects.py
│   │   ├── trainings.py
│   │   ├── visits.py
│   │   ├── media.py
│   │   └── stats.py
│   ├── services/             # Services métier
│   │   ├── email_service.py
│   │   ├── payment_service.py
│   │   └── media_service.py
│   ├── utils/                # Utilitaires
│   │   ├── helpers.py
│   │   ├── validators.py
│   │   └── decorators.py
│   ├── templates/            # Templates email
│   └── static/               # Fichiers statiques
├── deployment/               # Configuration déploiement
│   ├── docker-compose.yml
│   └── nginx.conf
├── migrations/               # Migrations DB
├── tests/                    # Tests
├── config.py                 # Configuration
├── requirements.txt          # Dépendances
├── Dockerfile
└── run.py                    # Point d'entrée

```

## Installation

### 1. Cloner le projet

```bash
cd backend
```

### 2. Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configuration

Copier `.env.example` vers `.env` et configurer les variables:

```bash
cp .env.example .env
```

### 5. Initialiser la base de données

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
flask init-db
flask seed-db
```

## Démarrage

### Mode développement

```bash
python run.py
```

Ou avec Flask CLI:

```bash
flask run
```

### Avec Docker

```bash
cd deployment
docker-compose up -d
```

## Endpoints API

### Authentification

- `POST /api/auth/register` - Inscription
- `POST /api/auth/login` - Connexion
- `POST /api/auth/refresh` - Rafraîchir token

### Projets

- `GET /api/projects` - Liste des projets
- `GET /api/projects/<id>` - Détail d'un projet
- `POST /api/projects` - Créer un projet (admin)
- `PUT /api/projects/<id>` - Modifier un projet (admin)
- `DELETE /api/projects/<id>` - Supprimer un projet (admin)

### Formations

- `GET /api/trainings` - Liste des formations
- `GET /api/trainings/<id>` - Détail d'une formation
- `GET /api/trainings/<id>/sessions` - Sessions d'une formation

### Visites

- `GET /api/visits` - Liste des types de visites
- `POST /api/visits/bookings` - Réserver une visite

### Statistiques

- `GET /api/stats` - Statistiques globales

## Tests

```bash
pytest
pytest --cov=app tests/
```

## Déploiement

### 1. Build Docker

```bash
docker build -t agriculture-backend .
```

### 2. Avec docker-compose

```bash
docker-compose -f deployment/docker-compose.yml up -d
```

## Variables d'environnement

Voir `.env.example` pour la liste complète.

## Sécurité

- JWT pour l'authentification
- Hashage bcrypt pour les mots de passe
- CORS configuré
- Validation des entrées
- Protection CSRF

## Licence

Propriétaire - Usage interne
