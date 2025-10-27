import { useState } from 'react'
import { Link } from 'react-router-dom'
import { FaFacebook, FaTwitter, FaInstagram, FaLinkedin } from 'react-icons/fa'
import { HiMail, HiPhone, HiLocationMarker } from 'react-icons/hi'
import toast from 'react-hot-toast'
import { newsletterService } from '../../services/api'

const Footer = () => {
  const [email, setEmail] = useState('')
  const [loading, setLoading] = useState(false)

  const handleNewsletterSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!email) return

    setLoading(true)
    try {
      const response = await newsletterService.subscribe(email)
      toast.success(response.data.message || 'Inscription réussie !')
      setEmail('')
    } catch (error: any) {
      toast.error(error.response?.data?.error || 'Erreur lors de l\'inscription')
    } finally {
      setLoading(false)
    }
  }

  return (
    <footer className="bg-charcoal text-white">
      <div className="container-custom py-12">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {/* À propos */}
          <div>
            <h3 className="text-xl font-bold mb-4 text-primary-400">
              Agroécologie & Permaculture
            </h3>
            <p className="text-gray-300 mb-4">
              Accompagnement de qualité pour une agriculture régénératrice et durable.
            </p>
            <div className="flex space-x-4">
              <a href="#" className="text-gray-300 hover:text-primary-400 transition-colors">
                <FaFacebook className="h-5 w-5" />
              </a>
              <a href="#" className="text-gray-300 hover:text-primary-400 transition-colors">
                <FaTwitter className="h-5 w-5" />
              </a>
              <a href="#" className="text-gray-300 hover:text-primary-400 transition-colors">
                <FaInstagram className="h-5 w-5" />
              </a>
              <a href="#" className="text-gray-300 hover:text-primary-400 transition-colors">
                <FaLinkedin className="h-5 w-5" />
              </a>
            </div>
          </div>

          {/* Liens rapides */}
          <div>
            <h3 className="text-lg font-bold mb-4">Liens rapides</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/presentation" className="text-gray-300 hover:text-primary-400">
                  Présentation
                </Link>
              </li>
              <li>
                <Link to="/services" className="text-gray-300 hover:text-primary-400">
                  Nos Services
                </Link>
              </li>
              <li>
                <Link to="/realisations" className="text-gray-300 hover:text-primary-400">
                  Réalisations
                </Link>
              </li>
              <li>
                <Link to="/formations" className="text-gray-300 hover:text-primary-400">
                  Formations
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h3 className="text-lg font-bold mb-4">Contact</h3>
            <ul className="space-y-3">
              <li className="flex items-start space-x-3">
                <HiLocationMarker className="h-5 w-5 text-primary-400 mt-1" />
                <span className="text-gray-300">Ziguinchor, Sénégal</span>
              </li>
              <li className="flex items-center space-x-3">
                <HiPhone className="h-5 w-5 text-primary-400" />
                <span className="text-gray-300">+221 77 266 02 67 / +221 78 323 28 79 / +221 778161138</span>
              </li>
              <li className="flex items-center space-x-3">
                <HiMail className="h-5 w-5 text-primary-400" />
                <span className="text-gray-300">contact@agriculture-permaculture.sn</span>
              </li>
            </ul>
          </div>

          {/* Newsletter */}
          <div>
            <h3 className="text-lg font-bold mb-4">Newsletter</h3>
            <p className="text-gray-300 mb-4">
              Inscrivez-vous pour recevoir nos actualités
            </p>
            <form className="space-y-2" onSubmit={handleNewsletterSubmit}>
              <input
                type="email"
                placeholder="Votre email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-4 py-2 rounded-lg bg-gray-800 text-white border border-gray-700 focus:outline-none focus:border-primary-400"
                required
              />
              <button type="submit" className="btn-primary w-full" disabled={loading}>
                {loading ? 'Inscription...' : 'S\'inscrire'}
              </button>
            </form>
          </div>
        </div>

        <div className="border-t border-gray-700 mt-8 pt-8 text-center text-gray-400">
          <p>© {new Date().getFullYear()} Agroécologie & Permaculture. Tous droits réservés.</p>
        </div>
      </div>
    </footer>
  )
}

export default Footer
