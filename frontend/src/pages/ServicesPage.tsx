const ServicesPage = () => {
  return (
    <div>
      <section className="bg-primary-600 text-white py-20">
        <div className="container-custom">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">Nos Services</h1>
          <p className="text-xl">Un accompagnement complet pour votre projet agricole</p>
        </div>
      </section>

      <section className="section">
        <div className="container-custom">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
            <div className="card p-8">
              <h3 className="text-2xl font-bold text-primary-700 mb-4">Formations</h3>
              <p className="text-gray-700 mb-4">
                Des formations pratiques et théoriques adaptées à tous les niveaux, du débutant à
                l'expert.
              </p>
              <a href="/formations" className="btn-primary">
                Voir les formations
              </a>
            </div>

            <div className="card p-8">
              <h3 className="text-2xl font-bold text-primary-700 mb-4">Visites de terrain</h3>
              <p className="text-gray-700 mb-4">
                Découvrez nos projets en action et apprenez directement sur le terrain.
              </p>
              <a href="/contact" className="btn-primary">
                Réserver une visite
              </a>
            </div>

            <div className="card p-8">
              <h3 className="text-2xl font-bold text-primary-700 mb-4">Accompagnement personnalisé</h3>
              <p className="text-gray-700 mb-4">
                Bénéficiez d'un suivi sur mesure pour la mise en place de votre projet.
              </p>
              <a href="/contact" className="btn-primary">
                Nous contacter
              </a>
            </div>

            <div className="card p-8">
              <h3 className="text-2xl font-bold text-primary-700 mb-4">Conseil et expertise</h3>
              <p className="text-gray-700 mb-4">
                Profitez de notre expertise pour optimiser votre exploitation agricole.
              </p>
              <a href="/contact" className="btn-primary">
                Demander un devis
              </a>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default ServicesPage
