# Guide Rapide: Déployer sur Railway (GRATUIT)

## 🚀 Déploiement en 10 minutes

### Étape 1: Préparer le projet pour Git

```bash
cd /home/dahaba/Téléchargements/AgriCulture-Permaculture

# Initialiser Git (si pas déjà fait)
git init

# Ajouter tous les fichiers
git add .

# Créer le premier commit
git commit -m "Initial commit - Agro Perma Sud"

# Créer la branche main
git branch -M main
```

### Étape 2: Créer un repository sur GitHub

1. Allez sur https://github.com
2. Cliquez sur "New repository"
3. Nom: `agro-perma-sud`
4. Laissez en "Public" (ou Private si vous préférez)
5. **NE PAS** cocher "Initialize with README"
6. Cliquez "Create repository"

### Étape 3: Pousser le code sur GitHub

```bash
# Remplacez USERNAME par votre nom d'utilisateur GitHub
git remote add origin https://github.com/USERNAME/agro-perma-sud.git

# Pousser le code
git push -u origin main
```

Si demandé, entrez vos identifiants GitHub (ou utilisez un token).

### Étape 4: Créer un compte Railway

1. Allez sur https://railway.app
2. Cliquez "Login"
3. Connectez-vous avec GitHub (recommandé)
4. Autorisez Railway à accéder à vos repositories

### Étape 5: Déployer le Backend

1. Sur Railway, cliquez **"New Project"**
2. Choisissez **"Deploy from GitHub repo"**
3. Sélectionnez le repository `agro-perma-sud`
4. Railway va détecter automatiquement Python

#### Configuration du Backend:

Dans les **Settings** du service:
- **Root Directory**: `backend`
- **Start Command**: `python run.py`
- **Port**: Railway le détecte automatiquement (5000)

#### Variables d'environnement (Settings > Variables):
```
FLASK_ENV=production
SECRET_KEY=votre-clé-secrète-super-longue-et-complexe
DATABASE_URL=${{Postgres.DATABASE_URL}}
PORT=5000
```

### Étape 6: Ajouter PostgreSQL

1. Dans votre projet Railway, cliquez **"+ New"**
2. Sélectionnez **"Database"** > **"Add PostgreSQL"**
3. Railway créera automatiquement la variable `DATABASE_URL`

### Étape 7: Déployer le Frontend

1. Dans le même projet, cliquez **"+ New"**
2. Choisissez **"GitHub Repo"** (même repository)
3. Railway va créer un nouveau service

#### Configuration du Frontend:

Dans les **Settings** du service:
- **Root Directory**: `frontend`
- **Build Command**: `npm install && npm run build`
- **Start Command**: `npm run preview`
- **Port**: 3000

#### Variables d'environnement:
```
VITE_API_URL=https://votre-backend.up.railway.app
NODE_ENV=production
```

### Étape 8: Configurer les domaines

1. Dans chaque service, allez dans **"Settings"** > **"Networking"**
2. Railway génère automatiquement des domaines HTTPS:
   - Backend: `backend-production-xxxx.up.railway.app`
   - Frontend: `frontend-production-xxxx.up.railway.app`

3. **Important**: Mettez à jour la variable `VITE_API_URL` du frontend avec l'URL du backend

### Étape 9: Configurer un domaine personnalisé (optionnel)

1. Dans le service Frontend, allez dans **"Settings"** > **"Domains"**
2. Cliquez **"Custom Domain"**
3. Entrez votre domaine: `agro-perma-sud.com`
4. Configurez les DNS chez votre registrar:
   ```
   Type: CNAME
   Name: @
   Value: frontend-production-xxxx.up.railway.app
   ```

---

## 🔧 Configuration avancée

### Fichier `.env` pour le Backend

Créez `backend/.env.example`:
```env
FLASK_ENV=production
SECRET_KEY=changez-cette-clé-secrète
DATABASE_URL=postgresql://user:password@host:port/database
PORT=5000
CORS_ORIGINS=https://votre-frontend.up.railway.app
```

### Mise à jour automatique

Railway redéploie automatiquement à chaque `git push` sur `main`!

---

## 📊 Monitoring

Dans Railway:
- **Logs**: Voir les logs en temps réel
- **Metrics**: CPU, RAM, Network
- **Deployments**: Historique des déploiements

---

## 💰 Coûts

### Plan Gratuit:
- ✅ 500 heures gratuites/mois
- ✅ 512 MB RAM par service
- ✅ SSL gratuit
- ✅ Domaine gratuit

### Calcul:
- Backend + Frontend = ~1 Go RAM total
- Si actif 24/7: ~720 heures/mois
- **Solution**: Passer au plan Hobby (5$/mois) si dépassement

---

## 🐛 Dépannage

### Le backend ne démarre pas:
```bash
# Vérifiez les logs dans Railway
# Assurez-vous que requirements.txt est à jour
pip freeze > backend/requirements.txt
git add backend/requirements.txt
git commit -m "Update requirements"
git push
```

### Le frontend ne trouve pas l'API:
- Vérifiez `VITE_API_URL` dans les variables d'environnement
- Ajoutez le domaine frontend dans les CORS du backend

### Base de données non connectée:
- Assurez-vous que la variable `DATABASE_URL` est bien définie
- Vérifiez que PostgreSQL est bien ajouté au projet

---

## ✅ Checklist Finale

- [ ] Code poussé sur GitHub
- [ ] Backend déployé sur Railway
- [ ] PostgreSQL configuré
- [ ] Frontend déployé sur Railway
- [ ] Variables d'environnement configurées
- [ ] Domaines HTTPS fonctionnels
- [ ] CORS configuré correctement
- [ ] Tests de l'API réussis
- [ ] Frontend accessible et fonctionnel

---

## 🎉 Résultat Final

Votre site sera accessible sur:
- **Frontend**: `https://agro-perma-sud-production.up.railway.app`
- **Backend API**: `https://agro-perma-sud-api-production.up.railway.app`

**HTTPS automatique, certificat SSL valide, gratuit!**

---

**Besoin d'aide?** Demandez-moi si vous rencontrez un problème!
