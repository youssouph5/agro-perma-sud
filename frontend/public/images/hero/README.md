# Images Hero Section

Ce dossier contient les images utilisées dans la section Hero de la page d'accueil.

## 📸 Images recommandées

### Format et dimensions
- **Format** : JPG ou WebP (pour de meilleures performances)
- **Dimensions recommandées** : 1200x800px minimum
- **Ratio** : 3:2 ou 4:3
- **Poids** : < 500KB (optimisé pour le web)

### Types d'images suggérées
1. **Agriculteur tenant des tomates** (comme l'image dans votre bannière)
2. **Jardin en permaculture**
3. **Formations pratiques**
4. **Systèmes agroforestiers**
5. **Récoltes biologiques**

## 🎨 Sources d'images gratuites

### Images actuellement utilisées (temporaires)
- **Unsplash** : https://unsplash.com/s/photos/permaculture
- Image par défaut : Photo de tomates fraîches

### Pour remplacer par vos propres images

1. **Placez votre image** dans ce dossier (ex: `hero-agriculture.jpg`)

2. **Mettez à jour HomePage.tsx** :
```tsx
<HeroSection
  title="Uvivers de l'Agroécologie..."
  subtitle="Formez-vous, inspirez-vous..."
  ctaText="Découvrir nos formations"
  ctaLink="/formations"
  layout="split"
  heroImage="/images/hero/hero-agriculture.jpg"  // ← Votre image
/>
```

## 🖼️ Images recommandées pour votre projet

### hero-main.jpg
L'image principale de la page d'accueil
- Suggestion : Agriculteur dans un jardin luxuriant
- Émotion : Confiance, authenticité, abondance

### hero-formations.jpg
Pour la page formations
- Suggestion : Groupe en formation pratique
- Émotion : Apprentissage, collaboration

### hero-realisations.jpg
Pour la page réalisations
- Suggestion : Vue d'ensemble d'un projet réussi
- Émotion : Accomplissement, résultats

## 🎯 Optimisation des images

### Avant d'ajouter une image :

1. **Redimensionner** à 1200px de large maximum
2. **Compresser** avec un outil comme :
   - TinyPNG : https://tinypng.com/
   - Squoosh : https://squoosh.app/
   - ImageOptim (Mac)

3. **Convertir en WebP** (optionnel mais recommandé) :
```bash
# Installer cwebp si nécessaire
sudo apt install webp

# Convertir l'image
cwebp -q 80 hero-agriculture.jpg -o hero-agriculture.webp
```

## 📚 Exemples d'utilisation

### Layout Split (recommandé)
```tsx
<HeroSection
  title="Votre titre"
  subtitle="Votre sous-titre"
  ctaText="Bouton d'action"
  ctaLink="/lien"
  layout="split"
  heroImage="/images/hero/votre-image.jpg"
/>
```

### Layout Centré (original)
```tsx
<HeroSection
  title="Votre titre"
  subtitle="Votre sous-titre"
  ctaText="Bouton d'action"
  ctaLink="/lien"
  layout="centered"
  backgroundImage="/images/hero/background.jpg"
/>
```

## 🎨 Suggestions de photos à prendre

Si vous prenez vos propres photos :

1. **Privilégiez la lumière naturelle** (golden hour)
2. **Montrez des visages souriants** (avec autorisation)
3. **Capturez l'action** (personnes en train de travailler)
4. **Montrez les résultats** (récoltes, jardins florissants)
5. **Incluez des gros plans** (mains dans la terre, légumes frais)

## 🔄 Images temporaires actuelles

Les images Unsplash sont utilisées temporairement. Remplacez-les par vos propres photos dès que possible pour :
- Authenticité
- Propriété intellectuelle
- Personnalisation de votre marque
