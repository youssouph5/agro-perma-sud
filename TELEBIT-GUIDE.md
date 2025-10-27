# Guide Telebit - Exposer votre site local sur Internet GRATUITEMENT

## 🌍 Qu'est-ce que Telebit?

Telebit est un service gratuit qui crée un tunnel sécurisé pour rendre votre serveur local accessible depuis n'importe où sur Internet, avec HTTPS automatique!

**Avantages:**
- ✅ **Totalement GRATUIT**
- ✅ **HTTPS automatique** avec certificat Let's Encrypt valide
- ✅ **Aucun port forwarding** nécessaire
- ✅ **Domaine personnalisé** possible
- ✅ **Parfait pour démos et tests**

**Inconvénients:**
- ⚠️ Votre machine doit rester allumée
- ⚠️ Dépend de votre connexion Internet
- ⚠️ Pas recommandé pour production 24/7

---

## 🚀 Installation de Telebit

### Méthode 1: Installation via npm (Recommandée)

```bash
# Installer Telebit globalement
sudo npm install -g telebit

# Ou sans sudo (méthode alternative)
npm install -g telebit
```

### Méthode 2: Installation via curl

```bash
curl -fsSL https://get.telebit.io/ | bash
```

---

## 🔧 Configuration

### Étape 1: Initialiser Telebit

```bash
# Lancer Telebit en mode interactif
telebit init

# Suivez les instructions:
# 1. Entrez votre email
# 2. Acceptez les conditions
# 3. Choisissez un nom de domaine
```

### Étape 2: Exposer votre site

#### Option A: Exposer le port 80 (HTTP → HTTPS)

```bash
# Telebit va automatiquement rediriger HTTP vers HTTPS
telebit http 80
```

#### Option B: Exposer le port 443 (HTTPS direct)

```bash
# Si vous avez déjà Nginx configuré avec HTTPS
telebit https 443
```

#### Option C: Exposer avec un domaine personnalisé

```bash
# Utiliser agro-perma-sud comme sous-domaine
telebit http 80 --servername agro-perma-sud
```

Votre site sera accessible sur:
- `https://agro-perma-sud.telebit.io`

---

## 🎯 Configuration pour votre projet

### Scénario 1: Exposer Nginx (recommandé)

Votre Nginx écoute déjà sur le port 80 et redirige vers vos services (frontend:3000, backend:5000).

```bash
# Assurez-vous que Nginx est démarré
sudo systemctl status nginx

# Exposer via Telebit
telebit http 80 --servername agro-perma-sud

# Votre site sera accessible sur:
# https://agro-perma-sud.telebit.io
```

### Scénario 2: Exposer directement le frontend

Si vous voulez exposer uniquement le frontend Vite:

```bash
# Exposer le port 3000
telebit http 3000 --servername agro-perma-sud

# Accessible sur:
# https://agro-perma-sud.telebit.io
```

---

## 📋 Configuration complète avec Nginx + Telebit

### 1. Démarrer vos services

```bash
# Terminal 1: Backend
cd backend
python run.py > backend.log 2>&1 &

# Terminal 2: Frontend
cd frontend
npm run dev &

# Terminal 3: Nginx
sudo systemctl start nginx
sudo systemctl status nginx
```

### 2. Vérifier que tout fonctionne localement

```bash
# Tester localement
curl http://localhost:80
# ou
curl https://agro-perma-sud.com
```

### 3. Lancer Telebit

```bash
# Exposer le port 80 (Nginx)
telebit http 80 --servername agro-perma-sud

# Telebit affichera l'URL publique:
# ✓ Forwarding https://agro-perma-sud.telebit.io => localhost:80
```

---

## 🔒 HTTPS et Certificats

**Bonne nouvelle**: Telebit génère automatiquement un certificat SSL Let's Encrypt valide!

- ❌ Plus d'avertissement "Non sécurisé"
- ✅ Certificat reconnu par tous les navigateurs
- ✅ HTTPS automatique

---

## 💡 Domaine Personnalisé

### Utiliser votre propre domaine (agro-perma-sud.com)

Si vous possédez déjà un domaine:

1. **Ajoutez un enregistrement CNAME** dans votre DNS:
   ```
   Type: CNAME
   Nom: @
   Valeur: agro-perma-sud.telebit.io
   ```

2. **Configurez Telebit**:
   ```bash
   telebit http 80 --servername agro-perma-sud.com
   ```

3. **Attendez la propagation DNS** (quelques minutes à quelques heures)

4. Votre site sera accessible sur `https://agro-perma-sud.com` **depuis n'importe où**!

---

## 🛠️ Commandes Utiles

```bash
# Lister les tunnels actifs
telebit list

# Arrêter tous les tunnels
telebit stop

# Redémarrer Telebit
telebit daemon restart

# Voir les logs
telebit logs

# Vérifier le statut
telebit status
```

---

## 🔄 Lancer Telebit au démarrage

### Créer un service systemd

```bash
# Créer le fichier service
sudo nano /etc/systemd/system/telebit.service
```

Contenu:
```ini
[Unit]
Description=Telebit Tunnel Service
After=network.target

[Service]
Type=simple
User=dahaba
WorkingDirectory=/home/dahaba
ExecStart=/usr/bin/telebit http 80 --servername agro-perma-sud
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Activer:
```bash
sudo systemctl daemon-reload
sudo systemctl enable telebit
sudo systemctl start telebit
sudo systemctl status telebit
```

---

## 📊 Comparaison: Telebit vs Railway

| Critère | Telebit | Railway |
|---------|---------|---------|
| **Prix** | 100% Gratuit | Gratuit (500h/mois) |
| **HTTPS** | ✅ Auto (Let's Encrypt) | ✅ Auto (Let's Encrypt) |
| **Domaine** | `.telebit.io` + custom | `.up.railway.app` + custom |
| **Machine** | Doit rester allumée | Serveur cloud 24/7 |
| **Latence** | Dépend de votre connexion | Serveurs optimisés |
| **Idéal pour** | Tests, démos | Production, validation |
| **Disponibilité** | Dépend de vous | 99.9% uptime |

---

## 🎓 Recommandations

### Pour validation de projet:
1. **Court terme (démo rapide)**: Utilisez **Telebit** (gratuit, rapide à setup)
2. **Moyen/long terme**: Utilisez **Railway** (plus fiable, toujours en ligne)

### Configuration idéale:
1. Développement local: `http://localhost:3000`
2. Tests avec amis/famille: `https://agro-perma-sud.telebit.io`
3. Validation officielle du projet: `https://agro-perma-sud.up.railway.app`
4. Production finale: Domaine personnalisé `https://agro-perma-sud.com`

---

## 🚀 Démarrage Rapide

```bash
# 1. Installer Telebit
curl -fsSL https://get.telebit.io/ | bash

# 2. Initialiser
telebit init

# 3. Démarrer vos services
cd /home/dahaba/Téléchargements/AgriCulture-Permaculture/backend
python run.py > backend.log 2>&1 &

cd /home/dahaba/Téléchargements/AgriCulture-Permaculture/frontend
npm run dev &

# 4. Exposer via Telebit
telebit http 80 --servername agro-perma-sud

# 5. Partager le lien!
# https://agro-perma-sud.telebit.io
```

---

## ⚠️ Limitations

- Votre ordinateur doit rester allumé
- Dépend de votre connexion Internet
- Pas recommandé pour un site en production 24/7
- Performance limitée par votre bande passante

---

**Prêt à essayer? Lancez:**
```bash
curl -fsSL https://get.telebit.io/ | bash
```
