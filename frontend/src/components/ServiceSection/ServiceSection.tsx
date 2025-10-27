import { ReactNode } from 'react'
import { motion } from 'framer-motion'

interface Service {
  icon: ReactNode
  title: string
  description: string
  link?: string
}

interface ServiceSectionProps {
  services: Service[]
}

const ServiceSection = ({ services }: ServiceSectionProps) => {
  return (
    <section className="section">
      <div className="container-custom">
        <h2 className="section-title">Nos Services</h2>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              className="card p-8 text-center hover:shadow-medium transition-all"
            >
              <div className="flex justify-center mb-6">
                <div className="w-20 h-20 bg-primary-100 rounded-full flex items-center justify-center text-primary-600">
                  {service.icon}
                </div>
              </div>

              <h3 className="text-2xl font-bold text-primary-800 mb-4">{service.title}</h3>

              <p className="text-gray-600 mb-6">{service.description}</p>

              {service.link && (
                <a
                  href={service.link}
                  className="inline-flex items-center text-primary-600 font-medium hover:text-primary-700"
                >
                  En savoir plus
                  <svg
                    className="w-4 h-4 ml-2"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M9 5l7 7-7 7"
                    />
                  </svg>
                </a>
              )}
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default ServiceSection
