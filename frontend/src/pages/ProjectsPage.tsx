import { useQuery } from 'react-query'
import { projectsService } from '@services/api'
import ProjectCard from '@components/ProjectCard/ProjectCard'

const ProjectsPage = () => {
  const { data, isLoading } = useQuery('projects', () => projectsService.getAll())

  return (
    <div>
      <section className="bg-primary-600 text-white py-20">
        <div className="container-custom">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">Nos Réalisations</h1>
          <p className="text-xl">Découvrez nos projets en permaculture et agriculture durable</p>
        </div>
      </section>

      <section className="section">
        <div className="container-custom">
          {isLoading ? (
            <div className="text-center py-12">
              <p className="text-lg text-gray-600">Chargement...</p>
            </div>
          ) : data?.data.projects && data.data.projects.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {data.data.projects.map((project, index) => (
                <ProjectCard key={project.id} project={project} index={index} />
              ))}
            </div>
          ) : (
            <div className="text-center py-12">
              <p className="text-lg text-gray-600">Aucun projet pour le moment</p>
            </div>
          )}
        </div>
      </section>
    </div>
  )
}

export default ProjectsPage
