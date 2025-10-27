# 📸 Guide d'Intégration des Images Hero

## 🎯 Ce qui a été fait

J'ai créé un nouveau layout pour la section Hero de votre page d'accueil qui permet d'**afficher une image à côté du texte**.

### ✅ Fonctionnalités ajoutées

1. **Deux types de layout** :
   - **Split** : Texte à gauche, image à droite (nouveau)
   - **Centered** : Texte centré avec background (original)

2. **Animations fluides** avec Framer Motion
3. **Badge flottant** sur l'image (100% Bio)
4. **Mini statistiques** sous le bouton CTA
5. **Effets décoratifs** (cercles colorés en arrière-plan)

## 🖼️ Aperçu du layout "Split"

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│  ┌─────────────────────┐    ┌─────────────────────┐      │
│  │                     │    │                     │      │
│  │  TITRE PRINCIPAL    │    │                     │      │
│  │                     │    │      IMAGE          │      │
│  │  Sous-titre         │    │                     │      │
│  │                     │    │    [Badge 100% Bio] │      │
│  │  [Bouton CTA]       │    │                     │      │
│  │                     │    └─────────────────────┘      │
│  │  10+    500+   50+  │                                  │
│  │  Stats  Stats  Stats│                                  │
│  │                     │                                  │
│  └─────────────────────┘                                  │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

## 🚀 Comment utiliser

### Méthode 1 : Utiliser une image en ligne (actuel)

L'image actuelle provient d'Unsplash (temporaire) :

```tsx
<HeroSection
  title="Votre titre"
  subtitle="Votre sous-titre"
  ctaText="Découvrir nos formations"
  ctaLink="/formations"
  layout="split"
  heroImage={HERO_IMAGES.mainFallback} // Image Unsplash
/>
```

### Méthode 2 : Utiliser votre propre image (recommandé)

1. **Placez votre image** dans le dossier :
   ```
   frontend/public/images/hero/
   ```

2. **Nommez votre image** (par exemple) :
   ```
   hero-main.jpg
   ```

3. **Mettez à jour le fichier** `frontend/src/constants/images.ts` :
   ```ts
   export const HERO_IMAGES = {
     main: '/images/hero/hero-main.jpg', // ✅ Activé
     mainFallback: 'https://...', // Garde comme backup
   }
   ```

4. **Utilisez-la dans HomePage.tsx** :
   ```tsx
   <HeroSection
     ...
     heroImage={HERO_IMAGES.main} // ← Votre image
   />
   ```

## 📐 Spécifications de l'image

### Dimensions recommandées
- **Largeur** : 800-1200px
- **Hauteur** : 600-900px
- **Ratio** : 3:2 ou 4:3
- **Poids** : < 500KB (optimisé)

### Format
- JPG (qualité 80-85%)
- WebP (recommandé pour performance)
- PNG (si transparence nécessaire)

### Contenu suggéré
✅ Agriculteur tenant des légumes frais
✅ Jardin en permaculture luxuriant
✅ Formations pratiques en action
✅ Récoltes abondantes
✅ Systèmes agroforestiers

## 🎨 Personnalisation

### Changer le badge flottant

Dans `HeroSection.tsx` ligne 144-154 :

```tsx
<div className="absolute bottom-6 left-6 bg-white/95 ...">
  <div className="flex items-center gap-3">
    <div className="w-12 h-12 bg-primary-600 rounded-full ...">
      <span className="text-white text-2xl">🌱</span> {/* Changez l'emoji */}
    </div>
    <div>
      <div className="font-bold text-primary-900">100% Bio</div> {/* Changez le texte */}
      <div className="text-sm text-gray-600">Agriculture naturelle</div> {/* Changez le sous-texte */}
    </div>
  </div>
</div>
```

### Changer les mini statistiques

Dans `HeroSection.tsx` ligne 110-123 :

```tsx
<div className="mt-12 grid grid-cols-3 gap-6">
  <div>
    <div className="text-3xl font-bold text-primary-700">10+</div> {/* Changez la valeur */}
    <div className="text-sm text-gray-600">Années d'expérience</div> {/* Changez le label */}
  </div>
  {/* Répétez pour les autres stats */}
</div>
```

### Désactiver les décorations géométriques

Commentez les lignes 157-159 dans `HeroSection.tsx` :

```tsx
{/*
<div className="absolute -z-10 top-8 -right-8 w-64 h-64 bg-primary-200 rounded-full blur-3xl opacity-50" />
<div className="absolute -z-10 bottom-8 -left-8 w-48 h-48 bg-accent-200 rounded-full blur-3xl opacity-50" />
*/}
```

## 🔄 Basculer entre les layouts

### Layout Split (avec image à côté)
```tsx
<HeroSection
  ...
  layout="split"
  heroImage={HERO_IMAGES.mainFallback}
/>
```

### Layout Centered (original)
```tsx
<HeroSection
  ...
  layout="centered"
  backgroundImage="/images/background.jpg"
/>
```

### Sans spécifier (défaut = centered)
```tsx
<HeroSection
  ...
  // Pas de layout spécifié = mode centré par défaut
/>
```

## 🛠️ Optimisation des images

### Compresser une image (Linux)

```bash
# Installer les outils
sudo apt install imagemagick webp

# Redimensionner et compresser JPG
convert votre-image.jpg -resize 1200x -quality 85 hero-main.jpg

# Convertir en WebP (meilleure compression)
cwebp -q 80 hero-main.jpg -o hero-main.webp
```

### Outils en ligne (sans installation)
- **TinyPNG** : https://tinypng.com/ (JPG/PNG)
- **Squoosh** : https://squoosh.app/ (tous formats)
- **Compressor.io** : https://compressor.io/

## 📱 Responsive

Le layout est automatiquement responsive :

- **Desktop (lg)** : Grille 2 colonnes (texte + image)
- **Tablette (md)** : Grille 1 colonne (image en dessous)
- **Mobile** : Grille 1 colonne (optimisé vertical)

## 🎯 Exemples de bonnes images

### Images gratuites haute qualité

1. **Unsplash** (actuel)
   - https://unsplash.com/s/photos/permaculture
   - https://unsplash.com/s/photos/organic-farming

2. **Pexels**
   - https://www.pexels.com/search/sustainable-agriculture/

3. **Pixabay**
   - https://pixabay.com/images/search/permaculture/

### Mots-clés de recherche
- "permaculture garden"
- "organic farming senegal"
- "sustainable agriculture"
- "farmer harvest vegetables"
- "agroecology"

## ✅ Checklist avant mise en production

- [ ] Remplacer l'image Unsplash par votre propre image
- [ ] Optimiser l'image (< 500KB)
- [ ] Tester sur mobile/tablette/desktop
- [ ] Vérifier que le texte reste lisible
- [ ] Personnaliser le badge flottant
- [ ] Ajuster les mini statistiques avec vos vraies données
- [ ] Vérifier l'alternative text (accessibilité)

## 🆘 Besoin d'aide ?

### L'image ne s'affiche pas
1. Vérifiez le chemin : `/images/hero/nom-fichier.jpg`
2. Vérifiez que l'image est bien dans `frontend/public/images/hero/`
3. Redémarrez le serveur de développement
4. Vérifiez la console du navigateur pour les erreurs

### L'image est trop lourde
1. Redimensionnez à 1200px de large max
2. Compressez avec TinyPNG ou Squoosh
3. Convertissez en WebP si possible

### Le layout ne ressemble pas à l'attendu
1. Vérifiez que `layout="split"` est bien défini
2. Vérifiez que `heroImage` est bien passé en prop
3. Videz le cache du navigateur (Ctrl+Shift+R)

## 📞 Contact

Pour toute question sur l'intégration des images, référez-vous à :
- Ce guide
- `frontend/public/images/hero/README.md`
- `frontend/src/constants/images.ts`
