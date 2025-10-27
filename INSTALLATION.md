# 🚀 Guide d'Installation - Agroécologie & Permaculture

Guide complet pour installer et démarrer le projet en local.

## 📋 Prérequis

Assurez-vous d'avoir installé :

- **Python** 3.11 ou supérieur
- **Node.js** 18 ou supérieur
- **PostgreSQL** 13 ou supérieur
- **Redis** 6 ou supérieur
- **Git**

### Vérification des versions

```bash
python3 --version  # Python 3.11+
node --version     # v18+
npm --version      # 9+
psql --version     # PostgreSQL 13+
redis-cli --version # Redis 6+
```

## 🗄️ Configuration de la base de données

### 1. Installer PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**macOS (avec Homebrew):**
```bash
brew install postgresql@13
brew services start postgresql@13
```

**Windows:**
Télécharger depuis [postgresql.org](https://www.postgresql.org/download/windows/)

### 2. Créer la base de données

```bash
# Se connecter à PostgreSQL
sudo -u postgres psql

# Créer l'utilisateur et la base
CREATE USER agriculture_user WITH PASSWORD 'votre_mot_de_passe';
CREATE DATABASE agriculture_db OWNER agriculture_user;
GRANT ALL PRIVILEGES ON DATABASE agriculture_db TO agriculture_user;
\q
```

## 🔴 Configuration de Redis

### Installer Redis

**Ubuntu/Debian:**
```bash
sudo apt install redis-server
sudo systemctl start redis-server
sudo systemctl enable redis-server
```

**macOS:**
```bash
brew install redis
brew services start redis
```

**Windows:**
Utiliser WSL ou télécharger depuis [redis.io](https://redis.io/download)

### Vérifier Redis

```bash
redis-cli ping
# Devrait retourner: PONG
```

## 🐍 Installation du Backend

### 1. Cloner le projet

```bash
git clone <votre-repo>
cd AgriCulture-Permaculture/backend
```

### 2. Créer l'environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

```bash
cp .env.example .env
```

Éditer le fichier `.env` :

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=votre-cle-secrete-tres-longue-et-aleatoire
JWT_SECRET_KEY=votre-jwt-secret-tres-long-et-aleatoire

# Base de données
DATABASE_URL=postgresql://agriculture_user:votre_mot_de_passe@localhost:5432/agriculture_db

# Redis
REDIS_URL=redis://localhost:6379/0

# Email (exemple avec Gmail)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=votre-email@gmail.com
MAIL_PASSWORD=votre-mot-de-passe-application
MAIL_DEFAULT_SENDER=noreply@agriculture-permaculture.fr

# Stripe (mode test)
STRIPE_PUBLIC_KEY=pk_test_votre_cle_publique
STRIPE_SECRET_KEY=sk_test_votre_cle_secrete

# URLs
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:5000
```

### 5. Initialiser la base de données

```bash
# Créer les migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Initialiser avec les données de base
flask init-db

# Ajouter des données de test
flask seed-db
```

### 6. Démarrer le backend

```bash
python run.py
```

Le backend sera accessible sur **http://localhost:5000**

### 7. Tester l'API

```bash
curl http://localhost:5000/health
# Devrait retourner: {"status":"healthy"}
```

## ⚛️ Installation du Frontend

### 1. Aller dans le dossier frontend

```bash
cd ../frontend
```

### 2. Installer les dépendances

```bash
npm install
```

### 3. Configurer les variables d'environnement

```bash
cp .env.example .env
```

Éditer le fichier `.env` :

```env
VITE_API_URL=http://localhost:5000/api
VITE_STRIPE_PUBLIC_KEY=pk_test_votre_cle_publique
```

### 4. Démarrer le frontend

```bash
npm run dev
```

Le frontend sera accessible sur **http://localhost:3000**

## ✅ Vérification de l'installation

### Backend

1. Ouvrir http://localhost:5000
2. Devrait afficher :
   ```json
   {
     "message": "API Agroécologie & Permaculture",
     "version": "1.0",
     "endpoints": {...}
   }
   ```

### Frontend

1. Ouvrir http://localhost:3000
2. La page d'accueil devrait s'afficher avec :
   - Navbar
   - Hero section
   - Services
   - Footer

### Test complet

1. Créer un compte utilisateur
2. Se connecter
3. Consulter les formations
4. Consulter les réalisations
5. Tester le formulaire de contact

## 🐳 Installation avec Docker (Alternative)

### 1. Installer Docker et Docker Compose

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2. Lancer avec Docker Compose

```bash
cd backend/deployment
docker-compose up -d
```

Cela démarrera :
- Backend Flask (port 5000)
- PostgreSQL (port 5432)
- Redis (port 6379)
- Nginx (ports 80 et 443)

### 3. Vérifier les conteneurs

```bash
docker-compose ps
```

### 4. Logs

```bash
docker-compose logs -f web
```

## 🛠️ Commandes utiles

### Backend

```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Créer une migration
flask db migrate -m "Description"

# Appliquer les migrations
flask db upgrade

# Réinitialiser la DB
flask db downgrade
flask db upgrade

# Ouvrir le shell Flask
flask shell

# Lancer les tests
pytest
pytest --cov=app tests/
```

### Frontend

```bash
# Démarrer en dev
npm run dev

# Build de production
npm run build

# Prévisualiser le build
npm run preview

# Linter
npm run lint

# Tests
npm run test
```

### Docker

```bash
# Démarrer les services
docker-compose up -d

# Arrêter les services
docker-compose down

# Rebuild des images
docker-compose build

# Voir les logs
docker-compose logs -f

# Exécuter une commande dans un conteneur
docker-compose exec web flask shell
```

## 🔧 Résolution des problèmes

### Erreur de connexion PostgreSQL

```bash
# Vérifier que PostgreSQL est démarré
sudo systemctl status postgresql

# Redémarrer PostgreSQL
sudo systemctl restart postgresql

# Vérifier les connexions
psql -U agriculture_user -d agriculture_db -h localhost
```

### Erreur de connexion Redis

```bash
# Vérifier que Redis est démarré
redis-cli ping

# Redémarrer Redis
sudo systemctl restart redis-server
```

### Port déjà utilisé

```bash
# Trouver le processus utilisant le port 5000
lsof -i :5000
# ou
netstat -ano | findstr :5000  # Windows

# Tuer le processus
kill -9 <PID>
```

### Erreurs d'import Python

```bash
# Réinstaller les dépendances
pip install --force-reinstall -r requirements.txt

# Vérifier l'environnement virtuel
which python
# Devrait pointer vers venv/bin/python
```

### Erreurs npm

```bash
# Nettoyer le cache
npm cache clean --force

# Supprimer node_modules et réinstaller
rm -rf node_modules package-lock.json
npm install
```

## 📚 Prochaines étapes

Après l'installation :

1. ✅ **Lire la documentation**
   - [README.md](README.md)
   - [backend/README.md](backend/README.md)
   - [frontend/README.md](frontend/README.md)

2. ✅ **Configurer les services tiers**
   - Créer un compte Stripe (mode test)
   - Configurer AWS S3 (optionnel)
   - Configurer Mailchimp (optionnel)

3. ✅ **Personnaliser le contenu**
   - Ajouter vos projets
   - Créer vos formations
   - Configurer les types de visites

4. ✅ **Déployer en production**
   - Configurer un serveur
   - Obtenir un nom de domaine
   - Installer les certificats SSL

## 💡 Conseils

- **Toujours utiliser l'environnement virtuel** pour Python
- **Ne jamais committer les fichiers .env** (contiennent les secrets)
- **Faire des sauvegardes régulières** de la base de données
- **Tester localement** avant de déployer en production
- **Utiliser Git** pour versionner votre code

## 🆘 Support

En cas de problème :

1. Vérifier les logs backend : `tail -f app.log`
2. Vérifier les logs frontend : Console du navigateur
3. Consulter la documentation
4. Contacter l'équipe technique

---

**Bonne installation ! 🚀**
