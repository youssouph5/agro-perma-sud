# 📸 Comment Ajouter Votre Propre Image Hero

## 🎯 Ce que vous avez maintenant

Votre page d'accueil affiche maintenant une **image en arrière-plan** avec le texte par-dessus, exactement comme dans votre bannière avec les tomates ! 🍅

```
┌──────────────────────────────────────────────┐
│                                              │
│         [IMAGE EN ARRIÈRE-PLAN]              │
│                                              │
│     Univers de l'Agroécologie et            │
│         de la Permaculture                   │
│                                              │
│   Formez-vous, inspirez-vous...             │
│                                              │
│      [Découvrir nos formations]              │
│                                              │
└──────────────────────────────────────────────┘
```

## ✅ Image actuelle

Pour l'instant, une **image temporaire d'Unsplash** est utilisée (tomates fraîches).

## 🚀 Pour utiliser VOTRE propre image

### Étape 1 : Préparer votre image

1. **Trouvez une belle photo** de :
   - Agriculteur tenant des légumes 🌱
   - Jardin en permaculture luxuriant 🌿
   - Formations pratiques 👨‍🌾
   - Récoltes abondantes 🥕

2. **Optimisez l'image** :
   - Largeur : 1920px (ou 1200px minimum)
   - Format : JPG ou WebP
   - Poids : < 500KB

### Étape 2 : Placer l'image dans le projet

Copiez votre image dans ce dossier :
```
frontend/public/images/hero/
```

Exemple :
```bash
cp ~/ma-photo.jpg frontend/public/images/hero/hero-main.jpg
```

### Étape 3 : Mettre à jour le code

Ouvrez le fichier :
```
frontend/src/constants/images.ts
```

Changez cette ligne :
```ts
// AVANT
main: '/images/hero/hero-main.jpg',

// Le code utilisera automatiquement cette image si elle existe !
```

OU directement dans `HomePage.tsx`, ligne 80 :
```tsx
// AVANT
heroImage={HERO_IMAGES.mainFallback}  // Image Unsplash

// APRÈS
heroImage="/images/hero/hero-main.jpg"  // Votre image
```

### Étape 4 : Tester

```bash
cd frontend
npm run dev
```

Visitez : http://localhost:3000

## 🎨 Personnalisation

### Changer l'obscurcissement de l'image

Dans `HeroSection.tsx` ligne 85 :

```tsx
// Plus sombre (texte plus visible)
backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url(${heroImage})`

// Plus clair (image plus visible)
backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url(${heroImage})`

// Actuel (équilibré)
backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${heroImage})`
```

### Changer la couleur du bouton

Dans `HeroSection.tsx` ligne 115 :

```tsx
// Bouton blanc avec texte vert (actuel)
className="bg-white text-primary-700 hover:bg-primary-50"

// Bouton jaune avec texte noir (comme votre bannière)
className="bg-yellow-400 text-gray-900 hover:bg-yellow-500"

// Bouton vert avec texte blanc
className="bg-primary-600 text-white hover:bg-primary-700"
```

## 🛠️ Outils pour optimiser l'image

### En ligne (gratuit)
1. **TinyPNG** : https://tinypng.com/
   - Glissez-déposez votre image
   - Téléchargez la version optimisée

2. **Squoosh** : https://squoosh.app/
   - Redimensionnez + compressez
   - Convertissez en WebP

### En ligne de commande (Linux)
```bash
# Installer les outils
sudo apt install imagemagick webp

# Redimensionner à 1920px de large
convert ma-photo.jpg -resize 1920x -quality 85 hero-main.jpg

# Ou convertir en WebP (meilleure compression)
cwebp -q 80 ma-photo.jpg -o hero-main.webp
```

## 📐 Recommandations de composition

Pour que le texte soit bien visible :

✅ **Bon** :
- Zone centrale assez uniforme (ciel, sol)
- Sujets sur les côtés
- Contraste modéré

❌ **À éviter** :
- Trop de détails au centre
- Texte difficile à lire
- Image trop chargée

## 🎯 Exemples d'images gratuites

Si vous n'avez pas encore votre propre photo :

1. **Unsplash** (haute qualité, gratuit)
   - https://unsplash.com/s/photos/permaculture
   - https://unsplash.com/s/photos/organic-farming-africa

2. **Pexels**
   - https://www.pexels.com/search/sustainable-agriculture/

3. **Pixabay**
   - https://pixabay.com/images/search/permaculture/

**Mots-clés de recherche** :
- "farmer holding vegetables"
- "permaculture garden"
- "sustainable agriculture senegal"
- "organic farming africa"

## ✅ Checklist rapide

- [ ] Image choisie/prise
- [ ] Image optimisée (< 500KB, 1920px)
- [ ] Image placée dans `frontend/public/images/hero/`
- [ ] Code mis à jour (HomePage.tsx ou images.ts)
- [ ] Testé en local (npm run dev)
- [ ] Vérifié que le texte est lisible
- [ ] Ajusté l'obscurcissement si nécessaire

## 🆘 Problèmes courants

### L'image ne s'affiche pas
✅ Vérifiez le chemin exact :
```
frontend/public/images/hero/hero-main.jpg
```

✅ Vérifiez le nom du fichier (sensible à la casse) :
- `hero-main.jpg` ✅
- `Hero-Main.JPG` ❌
- `hero_main.jpg` ❌

✅ Redémarrez le serveur :
```bash
# Ctrl+C puis
npm run dev
```

### L'image est floue
Utilisez une image plus grande (1920px minimum)

### Le texte n'est pas lisible
Augmentez l'obscurcissement :
```tsx
rgba(0, 0, 0, 0.7)  // Plus sombre
```

### L'image est trop lourde (lent à charger)
Compressez avec TinyPNG ou convertissez en WebP

## 🎉 C'est tout !

Une fois votre image ajoutée, vous aurez une **superbe page d'accueil** avec votre propre photo en arrière-plan ! 🌟

---

**Besoin d'aide ?** Consultez :
- [GUIDE_IMAGES_HERO.md](GUIDE_IMAGES_HERO.md) - Guide complet
- [frontend/public/images/hero/README.md](frontend/public/images/hero/README.md) - Détails techniques
