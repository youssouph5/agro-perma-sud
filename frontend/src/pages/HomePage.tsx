import { useQuery } from 'react-query'
import HeroSection from '@components/HeroSection/HeroSection'
import StatsCounter from '@components/StatsCounter/StatsCounter'
import ServiceSection from '@components/ServiceSection/ServiceSection'
import ProjectCard from '@components/ProjectCard/ProjectCard'
import { projectsService, statsService } from '@services/api'
import { HiAcademicCap, HiGlobeAlt, HiUserGroup, HiLightBulb } from 'react-icons/hi'
import { HERO_IMAGES } from '@/constants/images'

const HomePage = () => {
  const { data: projectsData } = useQuery('featured-projects', () =>
    projectsService.getAll({ featured: true })
  )

  const { data: statsData } = useQuery('global-stats', () => statsService.getGlobalStats())

  const services = [
    {
      icon: <HiAcademicCap className="h-12 w-12" />,
      title: 'Formations',
      description:
        'Formations pratiques en permaculture et agriculture durable pour tous les niveaux.',
      link: '/formations',
    },
    {
      icon: <HiGlobeAlt className="h-12 w-12" />,
      title: 'Visites de terrain',
      description:
        'Découvrez nos projets en action lors de visites guidées sur notre site.',
      link: '/services',
    },
    {
      icon: <HiUserGroup className="h-12 w-12" />,
      title: 'Accompagnement',
      description:
        'Conseil personnalisé pour la mise en place de votre projet agricole durable.',
      link: '/services',
    },
    {
      icon: <HiLightBulb className="h-12 w-12" />,
      title: 'Expertise',
      description:
        'Partage de connaissances et de techniques éprouvées en permaculture.',
      link: '/presentation',
    },
  ]

  const stats = [
    {
      label: 'Formations réalisées',
      value: statsData?.data.total_trainings || 0,
      suffix: '+',
    },
    {
      label: 'Visiteurs accueillis',
      value: statsData?.data.total_visits || 0,
      suffix: '+',
    },
    {
      label: 'Projets accompagnés',
      value: statsData?.data.total_projects || 0,
      suffix: '+',
    },
    {
      label: 'Abonnés newsletter',
      value: statsData?.data.total_subscribers || 0,
      suffix: '+',
    },
  ]

  return (
    <div>
      {/* Hero Section */}
      <HeroSection
        title="Univers de l'Agroécologie et de la Permaculture au Sénégal"
        subtitle="Formez-vous, inspirez-vous et transformez votre approche de l'agriculture pour une agriculture saine et durable"
        ctaText="Découvrir nos formations"
        ctaLink="/formations"
        layout="split"
        heroImage={HERO_IMAGES.mainFallback}
      />

      {/* Présentation rapide */}
      <section className="section">
        <div className="container-custom">
          <div className="max-w-3xl mx-auto text-center">
            <h2 className="section-title">Notre Mission</h2>
            <p className="text-lg text-gray-700 leading-relaxed">
              Nous accompagnons agriculteurs, particuliers et professionnels dans la transition
              vers une agriculture durable et régénératrice. À travers nos formations pratiques,
              visites de terrain et accompagnements personnalisés, nous partageons notre expertise
              en permaculture et agroécologie.
            </p>
          </div>
        </div>
      </section>

      {/* Services */}
      <ServiceSection services={services} />

      {/* Statistiques */}
      <StatsCounter stats={stats} />

      {/* Réalisations en vedette */}
      {projectsData?.data.projects && projectsData.data.projects.length > 0 && (
        <section className="section bg-gray-50">
          <div className="container-custom">
            <h2 className="section-title">Nos Réalisations</h2>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {projectsData.data.projects.slice(0, 3).map((project, index) => (
                <ProjectCard key={project.id} project={project} index={index} />
              ))}
            </div>

            <div className="text-center mt-12">
              <a href="/realisations" className="btn-primary">
                Voir toutes nos réalisations
              </a>
            </div>
          </div>
        </section>
      )}

      {/* Témoignages */}
      <section className="section">
        <div className="container-custom">
          <h2 className="section-title">Ils nous font confiance</h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[1, 2, 3].map((i) => (
              <div key={i} className="card p-8">
                <div className="flex items-center mb-4">
                  <div className="w-12 h-12 bg-primary-200 rounded-full mr-4" />
                  <div>
                    <h4 className="font-bold">Nom {i}</h4>
                    <p className="text-sm text-gray-600">Agriculteur</p>
                  </div>
                </div>
                <p className="text-gray-700 italic">
                  "Une formation de qualité qui m'a permis de transformer mon exploitation. Les
                  techniques enseignées sont concrètes et applicables immédiatement."
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Newsletter CTA */}
      <section className="section bg-primary-700 text-white">
        <div className="container-custom text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Restez informé de nos actualités
          </h2>
          <p className="text-xl mb-8 max-w-2xl mx-auto">
            Inscrivez-vous à notre newsletter pour recevoir conseils, actualités et invitations à
            nos événements.
          </p>

          <form className="max-w-md mx-auto flex gap-4">
            <input
              type="email"
              placeholder="Votre email"
              className="flex-1 px-6 py-3 rounded-lg text-gray-900"
            />
            <button type="submit" className="btn bg-white text-primary-700 hover:bg-gray-100">
              S'inscrire
            </button>
          </form>
        </div>
      </section>
    </div>
  )
}

export default HomePage
