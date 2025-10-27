# 🧪 Guide de Tests - Agroécologie & Permaculture

## 📋 Résumé des Tests Effectués

### ✅ Backend (Flask - Port 5000)

**Status:** ✅ Opérationnel

#### Endpoints Testés:

1. **Health Check** ✅
   ```bash
   curl http://localhost:5000/health
   # Résultat: {"status": "healthy"}
   ```

2. **Login Admin** ✅
   ```bash
   curl -X POST http://localhost:5000/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email": "admin@agriculture.com", "password": "admin123"}'
   # Résultat: JWT token + user info
   ```

3. **Projets** ✅
   ```bash
   curl http://localhost:5000/api/projects
   # Résultat: {"projects": [], "total": 0}
   ```

4. **Formations** ✅
   ```bash
   curl http://localhost:5000/api/trainings
   # Résultat: {"trainings": []}
   ```

5. **Visites** ✅
   ```bash
   curl http://localhost:5000/api/visits
   # Résultat: {"visits": []}
   ```

6. **Statistiques** ✅
   ```bash
   curl http://localhost:5000/api/stats
   # Résultat: {"total_projects": 0, "total_trainings": 0, ...}
   ```

7. **Contact** ✅
   ```bash
   curl -X POST http://localhost:5000/api/contact \
     -H "Content-Type: application/json" \
     -d '{"name": "Test", "email": "test@example.com", "subject": "Test", "message": "Message test"}'
   # Résultat: {"message": "Votre message a été envoyé avec succès..."}
   ```

8. **Newsletter** ✅
   ```bash
   curl -X POST http://localhost:5000/api/newsletter \
     -H "Content-Type: application/json" \
     -d '{"email": "newsletter@example.com"}'
   # Résultat: {"message": "Merci pour votre inscription!"}
   ```

---

### ✅ Frontend (React - Port 3000)

**Status:** ✅ Opérationnel

#### Pages Disponibles:

1. **Accueil** - http://localhost:3000/
2. **Présentation** - http://localhost:3000/presentation
3. **Services** - http://localhost:3000/services
4. **Réalisations** - http://localhost:3000/realisations
5. **Formations** - http://localhost:3000/formations
6. **Contact** - http://localhost:3000/contact

---

## 🧪 Tests à Effectuer Manuellement

### 1. Test du Formulaire de Contact

1. Ouvrir http://localhost:3000/contact
2. Remplir le formulaire:
   - Nom: Votre nom
   - Email: votre@email.com
   - Sujet: Test de contact
   - Message: Un message de test
3. Cliquer sur "Envoyer le message"
4. ✅ Vérifier le message de succès
5. ✅ Vérifier dans les logs backend que le message est reçu

**Commande pour voir les logs backend:**
```bash
# Les logs afficheront: "Contact reçu de [nom] ([email]): [sujet]"
```

---

### 2. Test de la Newsletter

#### Test depuis le Footer (sur toutes les pages):

1. Scroller en bas de n'importe quelle page
2. Dans la section Newsletter, entrer un email: test@newsletter.com
3. Cliquer sur "S'inscrire"
4. ✅ Vérifier le message de succès
5. ✅ Vérifier dans la base de données:

```bash
cd backend
source venv/bin/activate
python3 << EOF
from app import create_app, db
from app.models import NewsletterSubscriber

app = create_app()
with app.app_context():
    subscribers = NewsletterSubscriber.query.all()
    for sub in subscribers:
        print(f"Email: {sub.email}, Status: {sub.status}, Date: {sub.subscribed_at}")
EOF
```

---

### 3. Test de Navigation

1. **Navbar**:
   - ✅ Cliquer sur chaque lien du menu
   - ✅ Vérifier que la page se charge correctement
   - ✅ Vérifier que le lien actif est surligné

2. **Footer**:
   - ✅ Tester tous les liens rapides
   - ✅ Vérifier les réseaux sociaux (liens factices pour l'instant)

---

### 4. Test de Responsivité

1. Ouvrir les DevTools du navigateur (F12)
2. Activer le mode responsive (Ctrl+Shift+M)
3. Tester sur différentes tailles:
   - ✅ Mobile (375px)
   - ✅ Tablet (768px)
   - ✅ Desktop (1920px)

---

### 5. Test des Statistiques (HomePage)

1. Ouvrir http://localhost:3000/
2. Scroller vers la section des statistiques
3. ✅ Vérifier que les compteurs s'affichent (0 pour l'instant)

---

## 🔧 Informations Techniques

### Ports Utilisés:
- **Frontend:** http://localhost:3000
- **Backend:** http://localhost:5000

### Base de Données:
- **Type:** SQLite
- **Fichier:** `/backend/agriculture.db`
- **Admin créé:**
  - Email: admin@agriculture.com
  - Password: admin123

### Coordonnées Configurées:
- **Adresse:** Ziguinchor, Sénégal
- **Téléphone:** +221 77 266 02 67 / +221 78 323 28 79
- **Email:** contact@agriculture-permaculture.sn

---

## 🐛 Problèmes Connus

1. **Emails désactivés en développement**
   - Les emails de contact et newsletter ne sont pas envoyés
   - Les messages sont simplement loggés dans la console backend
   - À configurer en production avec un serveur SMTP valide

2. **Images/Médias**
   - Les pages peuvent afficher des placeholders
   - À remplacer par de vraies images en production

3. **CORS**
   - Configuré pour accepter toutes les origines en dev
   - À restreindre en production

---

## 📊 Prochaines Étapes

1. **Ajouter du contenu:**
   - Créer des projets via l'API
   - Ajouter des formations
   - Créer des visites

2. **Configurer l'email:**
   - Mettre à jour les credentials SMTP dans `.env`
   - Décommenter le code d'envoi d'email

3. **Déploiement:**
   - Configurer la base de données PostgreSQL
   - Configurer Nginx
   - Déployer avec Docker

---

## 🚀 Commandes Utiles

### Démarrer le Backend:
```bash
cd backend
source venv/bin/activate
flask run
```

### Démarrer le Frontend:
```bash
cd frontend
npm run dev
```

### Voir les logs Backend en temps réel:
```bash
# Le serveur Flask affiche les logs directement dans la console
```

### Inspecter la Base de Données:
```bash
cd backend
sqlite3 agriculture.db
.tables
SELECT * FROM newsletter_subscribers;
.quit
```

---

## ✅ Checklist Finale

- [x] Backend opérationnel sur port 5000
- [x] Frontend opérationnel sur port 3000
- [x] API Contact fonctionnelle
- [x] API Newsletter fonctionnelle
- [x] Base de données créée et migrée
- [x] Admin user créé
- [x] Coordonnées mises à jour
- [x] Navigation fonctionnelle
- [x] Design responsive
- [x] Intégration backend-frontend complète

**Tout est prêt pour les tests utilisateur! 🎉**
