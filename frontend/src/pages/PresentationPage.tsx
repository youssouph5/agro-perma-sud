const PresentationPage = () => {
  return (
    <div>
      <section className="section-title bg-primary-600 text-white py-20">
        <div className="container-custom">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">Présentation</h1>
          <p className="text-xl">Découvrez notre histoire et notre approche</p>
        </div>
      </section>

      <section className="section">
        <div className="container-custom">
          <div className="max-w-4xl mx-auto prose prose-lg">
            <h2>Notre Histoire</h2>
            <p>
              Fondée par des passionnés d'agriculture durable, notre plateforme est née de la
              volonté de partager notre expertise et d'accompagner la transition vers une
              agriculture respectueuse de l'environnement.
            </p>

            <h2>Notre Approche</h2>
            <p>
              Nous croyons fermement que l'agriculture peut être à la fois productive et
              régénératrice. Notre approche combine les principes de la permaculture avec les
              connaissances agronomiques modernes.
            </p>

            <h2>Notre Équipe</h2>
            <p>
              Une équipe pluridisciplinaire d'agronomes, permaculteurs et formateurs passionnés,
              tous engagés pour une agriculture durable.
            </p>
          </div>
        </div>
      </section>
    </div>
  )
}

export default PresentationPage
