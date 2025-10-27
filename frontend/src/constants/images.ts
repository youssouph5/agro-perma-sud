/**
 * Constantes pour les images utilisées dans l'application
 * Permet de gérer facilement les chemins d'images
 */

// Images Hero Section
export const HERO_IMAGES = {
  // Image principale de la page d'accueil
  main: '/images/hero/hero-main.jpg',

  // Image temporaire (Unsplash - à remplacer)
  mainFallback: 'https://images.unsplash.com/photo-1625246333195-78d9c38ad449?w=800&q=80',

  // Autres images pour différentes sections
  formations: '/images/hero/hero-formations.jpg',
  realisations: '/images/hero/hero-realisations.jpg',
  contact: '/images/hero/hero-contact.jpg',
}

// Images de fond (backgrounds)
export const BACKGROUND_IMAGES = {
  permaculture: 'https://images.unsplash.com/photo-1464226184884-fa280b87c399?w=1200&q=80',
  garden: 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&q=80',
  harvest: 'https://images.unsplash.com/photo-1574943320219-553eb213f72d?w=1200&q=80',
}

// Images pour les cartes et sections
export const SECTION_IMAGES = {
  defaultProject: 'https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?w=600&q=80',
  defaultTraining: 'https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?w=600&q=80',
}

// Placeholder pour les images manquantes
export const PLACEHOLDER_IMAGES = {
  default: 'https://via.placeholder.com/800x600/4CAF50/ffffff?text=Agriculture+Permaculture',
  avatar: 'https://via.placeholder.com/150/4CAF50/ffffff?text=Avatar',
}

/**
 * Helper pour obtenir l'image avec fallback
 * @param imagePath - Chemin de l'image préféré
 * @param fallback - Image de secours si la principale n'existe pas
 */
export const getImageWithFallback = (imagePath: string, fallback: string): string => {
  // Dans une vraie application, on pourrait vérifier si l'image existe
  // Pour l'instant, on utilise toujours le fallback pour les images locales non configurées
  if (imagePath.startsWith('/images/hero/') && !imagePath.includes('README')) {
    // Vérifier si l'image locale existe (simulation)
    // Dans un vrai cas, vous utiliseriez une vérification côté serveur
    return fallback
  }
  return imagePath
}

/**
 * Helper pour obtenir les attributs d'image optimisés
 */
export const getOptimizedImageProps = (src: string, alt: string) => ({
  src,
  alt,
  loading: 'lazy' as const,
  decoding: 'async' as const,
})
