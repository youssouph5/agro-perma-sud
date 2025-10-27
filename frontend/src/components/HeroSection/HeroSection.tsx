import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

interface HeroSectionProps {
  title: string
  subtitle: string
  ctaText?: string
  ctaLink?: string
  backgroundImage?: string
  heroImage?: string // Nouvelle prop pour l'image d'accompagnement
  layout?: 'centered' | 'split' // Type de layout
}

const HeroSection = ({
  title,
  subtitle,
  ctaText,
  ctaLink,
  backgroundImage,
  heroImage,
  layout = 'centered'
}: HeroSectionProps) => {

  // Layout centré (original)
  if (layout === 'centered' || !heroImage) {
    return (
      <section
        className="relative h-[600px] flex items-center justify-center bg-cover bg-center"
        style={{
          backgroundImage: backgroundImage
            ? `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${backgroundImage})`
            : 'linear-gradient(135deg, #2E7D32 0%, #4CAF50 100%)',
        }}
      >
        <div className="container-custom text-center text-white z-10">
          <motion.h1
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-4xl md:text-5xl lg:text-6xl font-bold mb-6"
          >
            {title}
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-xl md:text-2xl mb-8 max-w-3xl mx-auto"
          >
            {subtitle}
          </motion.p>

          {ctaText && ctaLink && (
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.4 }}
            >
              <Link
                to={ctaLink}
                className="inline-block bg-white text-primary-700 px-8 py-4 rounded-lg font-bold text-lg hover:bg-primary-50 transition-colors shadow-lg"
              >
                {ctaText}
              </Link>
            </motion.div>
          )}
        </div>

        {/* Scroll indicator */}
        <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2">
          <div className="w-6 h-10 border-2 border-white rounded-full flex justify-center">
            <div className="w-1 h-3 bg-white rounded-full mt-2 animate-bounce" />
          </div>
        </div>
      </section>
    )
  }

  // Layout split - Image en arrière-plan avec texte par-dessus
  return (
    <section
      className="relative h-[600px] flex items-center justify-center bg-cover bg-center"
      style={{
        backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${heroImage})`,
      }}
    >
      <div className="container-custom text-center text-white z-10">
        <motion.h1
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-4xl md:text-5xl lg:text-6xl font-bold mb-6"
        >
          {title}
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="text-xl md:text-2xl mb-8 max-w-3xl mx-auto"
        >
          {subtitle}
        </motion.p>

        {ctaText && ctaLink && (
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
          >
            <Link
              to={ctaLink}
              className="inline-block bg-white text-primary-700 px-8 py-4 rounded-lg font-bold text-lg hover:bg-primary-50 transition-colors shadow-lg"
            >
              {ctaText}
            </Link>
          </motion.div>
        )}
      </div>

      {/* Scroll indicator */}
      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2">
        <div className="w-6 h-10 border-2 border-white rounded-full flex justify-center">
          <div className="w-1 h-3 bg-white rounded-full mt-2 animate-bounce" />
        </div>
      </div>
    </section>
  )
}

export default HeroSection
