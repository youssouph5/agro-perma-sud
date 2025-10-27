import { Link } from 'react-router-dom'
import { HiLocationMarker, HiCalendar } from 'react-icons/hi'
import { motion } from 'framer-motion'

interface Project {
  id: number
  title: string
  slug: string
  short_description: string
  location: string
  start_date: string
  featured: boolean
  image?: string
}

interface ProjectCardProps {
  project: Project
  index?: number
}

const ProjectCard = ({ project, index = 0 }: ProjectCardProps) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: index * 0.1 }}
      className="card group"
    >
      {/* Image */}
      <div className="relative h-64 overflow-hidden">
        {project.image ? (
          <img
            src={project.image}
            alt={project.title}
            className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
          />
        ) : (
          <div className="w-full h-full bg-gradient-to-br from-primary-400 to-primary-600 flex items-center justify-center">
            <span className="text-white text-6xl font-bold opacity-20">
              {project.title.charAt(0)}
            </span>
          </div>
        )}
        {project.featured && (
          <div className="absolute top-4 right-4 bg-secondary text-white px-3 py-1 rounded-full text-sm font-medium">
            À la une
          </div>
        )}
      </div>

      {/* Content */}
      <div className="p-6">
        <h3 className="text-xl font-bold text-primary-800 mb-2 group-hover:text-primary-600 transition-colors">
          {project.title}
        </h3>

        <p className="text-gray-600 mb-4 line-clamp-3">{project.short_description}</p>

        <div className="flex items-center text-sm text-gray-500 space-x-4 mb-4">
          <div className="flex items-center">
            <HiLocationMarker className="h-4 w-4 mr-1" />
            {project.location}
          </div>
          <div className="flex items-center">
            <HiCalendar className="h-4 w-4 mr-1" />
            {new Date(project.start_date).getFullYear()}
          </div>
        </div>

        <Link
          to={`/realisations/${project.slug}`}
          className="inline-flex items-center text-primary-600 font-medium hover:text-primary-700"
        >
          Voir le projet
          <svg
            className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
          </svg>
        </Link>
      </div>
    </motion.div>
  )
}

export default ProjectCard
