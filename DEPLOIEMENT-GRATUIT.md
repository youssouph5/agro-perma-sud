# Guide de Déploiement GRATUIT - Agro Perma Sud

Ce guide vous explique comment déployer gratuitement votre plateforme avec un domaine et un certificat SSL valide.

## 🎯 Options de Déploiement Gratuit

### Option 1: Railway (RECOMMANDÉE) ⭐
**Avantages:**
- 500 heures gratuites/mois (suffisant pour un projet en validation)
- Déploiement automatique depuis GitHub
- SSL gratuit automatique
- Support PostgreSQL gratuit
- Sous-domaine gratuit: `agro-perma-sud.up.railway.app`

**Étapes:**

1. **Créer un compte sur Railway**
   - Allez sur https://railway.app
   - Connectez-vous avec GitHub

2. **Préparer le projet**
   ```bash
   # Créer un repository GitHub si pas déjà fait
   cd /home/dahaba/Téléchargements/AgriCulture-Permaculture
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <votre-repo-github>
   git push -u origin main
   ```

3. **Déployer le Backend**
   - Sur Railway, cliquez "New Project"
   - Sélectionnez "Deploy from GitHub repo"
   - Choisissez votre repository
   - Railway détectera automatiquement Python
   - Ajoutez les variables d'environnement nécessaires

4. **Déployer le Frontend**
   - Ajoutez un nouveau service dans le même projet
   - Sélectionnez le même repository
   - Configurez le build command: `cd frontend && npm install && npm run build`
   - Start command: `cd frontend && npm run preview`

5. **Configurer la base de données**
   - Ajoutez PostgreSQL depuis le menu "New Service"
   - Railway fournira automatiquement l'URL de connexion

---

### Option 2: Render (Alternative solide)
**Avantages:**
- Plan gratuit permanent
- SSL automatique
- Base de données PostgreSQL gratuite (limite: 90 jours)
- Sous-domaine: `agro-perma-sud.onrender.com`

**Étapes:**
1. Allez sur https://render.com
2. Créez un compte
3. Créez un "Web Service" pour le backend
4. Créez un "Static Site" pour le frontend
5. Ajoutez une base de données PostgreSQL

---

### Option 3: Vercel (Frontend) + Heroku/Railway (Backend)
**Avantages:**
- Vercel est excellent pour React
- SSL automatique
- Déploiement ultra-rapide
- Sous-domaine: `agro-perma-sud.vercel.app`

---

## 🌐 Domaine Gratuit

### Option A: Sous-domaine gratuit des hébergeurs
Utilisez directement:
- `agro-perma-sud.up.railway.app` (Railway)
- `agro-perma-sud.onrender.com` (Render)
- `agro-perma-sud.vercel.app` (Vercel)

### Option B: Domaine gratuit .tk, .ml, .ga, .cf ou .gq
- Allez sur https://www.freenom.com
- Cherchez "agro-perma-sud.tk" (ou .ml, .ga, etc.)
- Enregistrez gratuitement pour 12 mois
- Configurez les DNS pour pointer vers votre hébergeur

### Option C: Domaine personnalisé pas cher (~10€/an)
- OVH, Gandi, Namecheap: ~8-12€/an pour un .com
- Possibilité d'acheter "agro-perma-sud.com" ou "agro-perma-sud.fr"

---

## 🔒 Certificat SSL Gratuit

Tous les hébergeurs mentionnés (Railway, Render, Vercel) fournissent **automatiquement** un certificat SSL Let's Encrypt gratuit et valide. Aucune configuration nécessaire!

Si vous utilisez votre propre serveur VPS, utilisez Certbot:

```bash
# Installer Certbot
sudo apt install certbot python3-certbot-nginx

# Obtenir un certificat SSL (remplacez le domaine)
sudo certbot --nginx -d agro-perma-sud.com -d www.agro-perma-sud.com

# Le renouvellement est automatique!
```

---

## 📦 Fichiers de Configuration Nécessaires

### 1. Backend: `Procfile` (pour Heroku/Render)
```
web: cd backend && python run.py
```

### 2. Backend: `railway.json` (pour Railway)
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "cd backend && python run.py",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### 3. Frontend: Configuration Vercel
Créer `vercel.json`:
```json
{
  "buildCommand": "cd frontend && npm install && npm run build",
  "outputDirectory": "frontend/dist",
  "framework": "vite",
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "https://votre-backend.up.railway.app/api/$1"
    }
  ]
}
```

---

## 🚀 Déploiement Recommandé: Railway

### Avantages de Railway:
1. ✅ Backend + Frontend + DB dans un seul projet
2. ✅ SSL automatique gratuit
3. ✅ 500 heures gratuites/mois
4. ✅ Déploiement en quelques clics
5. ✅ Logs en temps réel
6. ✅ Domaine personnalisé supporté

### Coût après validation du projet:
- Plan Hobby: 5$/mois (si besoin de plus de 500h)
- Domaine .com: ~10€/an

---

## 📊 Comparatif des Options Gratuites

| Hébergeur | Backend | Frontend | Database | SSL | Domaine | Limite |
|-----------|---------|----------|----------|-----|---------|--------|
| **Railway** | ✅ | ✅ | ✅ PostgreSQL | ✅ Auto | Sous-domaine gratuit | 500h/mois |
| **Render** | ✅ | ✅ | ✅ PostgreSQL (90j) | ✅ Auto | Sous-domaine gratuit | Permanent |
| **Vercel** | ❌ | ✅ | ❌ | ✅ Auto | Sous-domaine gratuit | Permanent |
| **Heroku** | ✅ | ❌ | ⚠️ Payant | ✅ Auto | Sous-domaine gratuit | 550h/mois |

---

## 🎓 Pour Validation de Projet

**Je recommande:**
1. **Railway** pour tout héberger (le plus simple)
2. Utiliser le sous-domaine gratuit `agro-perma-sud.up.railway.app`
3. Certificat SSL automatique (HTTPS fonctionnel)
4. Coût: **0€/mois** pendant la validation

**Après validation:**
- Acheter un vrai domaine: `agro-perma-sud.com` (~10€/an)
- Passer à Railway Hobby si besoin: 5$/mois
- Total: ~15€/an pour un site professionnel complet

---

## 📝 Prochaines Étapes

1. Choisir Railway comme hébergeur
2. Créer un compte GitHub et pousser le code
3. Déployer sur Railway en 5 minutes
4. Partager le lien `https://agro-perma-sud.up.railway.app`
5. Configurer Google Analytics et Search Console pour le référencement

**Voulez-vous que je vous aide à déployer sur Railway maintenant?**
