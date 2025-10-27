# Frontend - Plateforme Agroécologie & Permaculture

Interface utilisateur React + TypeScript pour la plateforme d'agriculture durable et permaculture.

## Technologies

- **Framework**: React 18.2 + TypeScript
- **Build Tool**: Vite 5
- **Styling**: Tailwind CSS 3.3
- **Routing**: React Router v6
- **State Management**: Zustand + React Query
- **HTTP Client**: Axios
- **Animations**: Framer Motion
- **Forms**: React Hook Form + Zod
- **UI Components**: Custom components inspirés du style ANCAR

## Structure du projet

```
frontend/
├── src/
│   ├── components/         # Composants réutilisables
│   │   ├── Navbar/
│   │   ├── Footer/
│   │   ├── HeroSection/
│   │   ├── StatsCounter/
│   │   ├── ProjectCard/
│   │   └── ServiceSection/
│   ├── pages/              # Pages de l'application
│   │   ├── HomePage.tsx
│   │   ├── PresentationPage.tsx
│   │   ├── ServicesPage.tsx
│   │   ├── ProjectsPage.tsx
│   │   ├── TrainingsPage.tsx
│   │   └── ContactPage.tsx
│   ├── services/           # Services API
│   │   └── api.ts
│   ├── hooks/              # Custom hooks
│   ├── utils/              # Utilitaires
│   ├── styles/             # Styles globaux
│   │   └── index.css
│   ├── App.tsx
│   └── main.tsx
├── public/                 # Fichiers statiques
├── index.html
├── package.json
├── tailwind.config.js
├── vite.config.ts
└── tsconfig.json
```

## Installation

### 1. Installer les dépendances

```bash
cd frontend
npm install
```

### 2. Configuration

Copier `.env.example` vers `.env` :

```bash
cp .env.example .env
```

Configurer les variables :

```env
VITE_API_URL=http://localhost:5000/api
VITE_STRIPE_PUBLIC_KEY=votre_cle_publique_stripe
```

### 3. Démarrage

```bash
npm run dev
```

L'application sera accessible sur `http://localhost:3000`

## Scripts disponibles

- `npm run dev` - Démarrer le serveur de développement
- `npm run build` - Build de production
- `npm run preview` - Prévisualiser le build de production
- `npm run lint` - Linter le code
- `npm run test` - Lancer les tests

## Pages principales

### 1. Page d'accueil (`/`)
- Hero section avec CTA
- Présentation de la mission
- Services en vedette
- Statistiques animées
- Réalisations en vedette
- Témoignages
- Newsletter CTA

### 2. Présentation (`/presentation`)
- Histoire de l'organisation
- Approche et méthodologie
- Équipe

### 3. Services (`/services`)
- Formations
- Visites de terrain
- Accompagnement personnalisé
- Conseil et expertise

### 4. Réalisations (`/realisations`)
- Liste des projets
- Filtres par statut, localisation
- Cards avec informations clés

### 5. Formations (`/formations`)
- Catalogue des formations
- Détails (durée, prix, niveau)
- Système de réservation

### 6. Contact (`/contact`)
- Formulaire de contact
- Informations de contact
- Carte interactive

## Thème et Design

Le design est inspiré du modèle ANCAR avec :

### Palette de couleurs
- **Vert principal** : #2E7D32 (confiance, institutionnel)
- **Vert secondaire** : #4CAF50 (accents, actions)
- **Terre/Beige** : #8D6E63 (chaleur)
- **Blanc pur** : #FFFFFF
- **Gris charbon** : #2C2C2C

### Typographie
- **Headers** : Roboto / Montserrat
- **Corps** : Open Sans / Source Sans Pro

### Composants
- Boutons avec variantes (primary, secondary, outline)
- Cards avec hover effects
- Inputs et formulaires stylisés
- Animations fluides avec Framer Motion

## API Integration

Les appels API sont gérés via Axios avec :
- Intercepteurs pour JWT
- Gestion automatique du refresh token
- Gestion d'erreurs centralisée
- React Query pour le cache et la synchronisation

## Responsive Design

- **Mobile First** : Design optimisé pour mobile
- **Breakpoints** :
  - Mobile : < 768px
  - Tablet : 768px - 1024px
  - Desktop : > 1024px
- Navigation adaptative
- Images optimisées

## Build et Déploiement

### Build de production

```bash
npm run build
```

Les fichiers de production seront dans le dossier `dist/`

### Déploiement

Le projet peut être déployé sur :
- Vercel
- Netlify
- GitHub Pages
- Serveur statique avec Nginx

Exemple de configuration Nginx :

```nginx
server {
    listen 80;
    server_name votre-domaine.com;
    root /var/www/agriculture-frontend/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

## Performance

- Lazy loading des images
- Code splitting automatique avec Vite
- Compression des assets
- Cache API avec React Query
- Optimisation des animations

## Accessibilité

- Navigation au clavier
- Attributs ARIA
- Contraste des couleurs WCAG AA
- Textes alternatifs pour les images

## Licence

Propriétaire - Usage interne
