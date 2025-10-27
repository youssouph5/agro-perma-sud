import { useState } from 'react'
import { HiMail, HiPhone, HiLocationMarker } from 'react-icons/hi'
import toast from 'react-hot-toast'
import { contactService } from '../services/api'

const ContactPage = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
  })
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)

    try {
      const response = await contactService.sendMessage(formData)
      toast.success(response.data.message || 'Message envoyé avec succès !')
      setFormData({ name: '', email: '', subject: '', message: '' })
    } catch (error: any) {
      toast.error(error.response?.data?.error || 'Erreur lors de l\'envoi du message')
    } finally {
      setLoading(false)
    }
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  return (
    <div>
      <section className="bg-primary-600 text-white py-20">
        <div className="container-custom">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">Contactez-nous</h1>
          <p className="text-xl">Nous sommes à votre écoute</p>
        </div>
      </section>

      <section className="section">
        <div className="container-custom">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
            {/* Formulaire */}
            <div>
              <h2 className="text-2xl font-bold text-primary-800 mb-6">Envoyez-nous un message</h2>

              <form onSubmit={handleSubmit} className="space-y-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Nom</label>
                  <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    className="input"
                    required
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
                  <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    className="input"
                    required
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Sujet</label>
                  <input
                    type="text"
                    name="subject"
                    value={formData.subject}
                    onChange={handleChange}
                    className="input"
                    required
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Message</label>
                  <textarea
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    className="textarea"
                    rows={6}
                    required
                  />
                </div>

                <button type="submit" className="btn-primary w-full" disabled={loading}>
                  {loading ? 'Envoi en cours...' : 'Envoyer le message'}
                </button>
              </form>
            </div>

            {/* Informations de contact */}
            <div>
              <h2 className="text-2xl font-bold text-primary-800 mb-6">Nos coordonnées</h2>

              <div className="space-y-6">
                <div className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center flex-shrink-0">
                    <HiLocationMarker className="h-6 w-6 text-primary-600" />
                  </div>
                  <div>
                    <h3 className="font-bold text-lg mb-1">Adresse</h3>
                    <p className="text-gray-600">Ziguinchor, Sénégal</p>
                  </div>
                </div>

                <div className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center flex-shrink-0">
                    <HiPhone className="h-6 w-6 text-primary-600" />
                  </div>
                  <div>
                    <h3 className="font-bold text-lg mb-1">Téléphone</h3>
                    <p className="text-gray-600">
                      +221 77 266 02 67
                      <br />
                      +221 78 323 28 79
                      <br />
                      +221 77 816 11 38
                    </p>
                  </div>
                </div>

                <div className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center flex-shrink-0">
                    <HiMail className="h-6 w-6 text-primary-600" />
                  </div>
                  <div>
                    <h3 className="font-bold text-lg mb-1">Email</h3>
                    <p className="text-gray-600">contact@agriculture-permaculture.sn</p>
                  </div>
                </div>
              </div>

              {/* Carte */}
              <div className="mt-8">
                <div className="bg-gray-200 h-64 rounded-lg flex items-center justify-center">
                  <p className="text-gray-500">Carte interactive</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default ContactPage
