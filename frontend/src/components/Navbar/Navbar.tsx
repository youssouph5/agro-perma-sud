import { Link, useLocation } from 'react-router-dom'
import { useState } from 'react'
import { HiMenu, HiX } from 'react-icons/hi'

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false)
  const location = useLocation()

  const navigation = [
    { name: 'Accueil', href: '/' },
    { name: 'Présentation', href: '/presentation' },
    { name: 'Nos Services', href: '/services' },
    { name: 'Réalisations', href: '/realisations' },
    { name: 'Formations', href: '/formations' },
    { name: 'Contact', href: '/contact' },
  ]

  const isActive = (path: string) => location.pathname === path

  return (
    <nav className="bg-white shadow-md sticky top-0 z-50">
      <div className="container-custom">
        <div className="flex justify-between items-center h-20">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-3">
            <div className="w-12 h-12 bg-primary-500 rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-xl">AP</span>
            </div>
            <div className="hidden md:block">
              <p className="font-heading font-bold text-xl text-primary-800">
                Agroécologie & Permaculture
              </p>
              <p className="text-sm text-gray-600">Pour une agriculture durable</p>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden lg:flex items-center space-x-1">
            {navigation.map((item) => (
              <Link
                key={item.name}
                to={item.href}
                className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                  isActive(item.href)
                    ? 'bg-primary-500 text-white'
                    : 'text-gray-700 hover:bg-primary-50 hover:text-primary-700'
                }`}
              >
                {item.name}
              </Link>
            ))}
          </div>

          {/* CTA Button */}
          <div className="hidden lg:block">
            <Link to="/contact" className="btn-primary">
              Nous contacter
            </Link>
          </div>

          {/* Mobile menu button */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="lg:hidden p-2 rounded-lg text-gray-700 hover:bg-primary-50"
          >
            {isOpen ? <HiX className="h-6 w-6" /> : <HiMenu className="h-6 w-6" />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <div className="lg:hidden py-4 border-t border-gray-200">
            <div className="flex flex-col space-y-2">
              {navigation.map((item) => (
                <Link
                  key={item.name}
                  to={item.href}
                  onClick={() => setIsOpen(false)}
                  className={`px-4 py-3 rounded-lg font-medium transition-colors ${
                    isActive(item.href)
                      ? 'bg-primary-500 text-white'
                      : 'text-gray-700 hover:bg-primary-50'
                  }`}
                >
                  {item.name}
                </Link>
              ))}
              <Link
                to="/contact"
                onClick={() => setIsOpen(false)}
                className="btn-primary mx-4 mt-2"
              >
                Nous contacter
              </Link>
            </div>
          </div>
        )}
      </div>
    </nav>
  )
}

export default Navbar
