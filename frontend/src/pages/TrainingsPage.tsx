import { useQuery } from 'react-query'
import { trainingsService } from '@services/api'

const TrainingsPage = () => {
  const { data, isLoading } = useQuery('trainings', () => trainingsService.getAll())

  return (
    <div>
      <section className="bg-primary-600 text-white py-20">
        <div className="container-custom">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">Nos Formations</h1>
          <p className="text-xl">Apprenez la permaculture et l'agriculture durable</p>
        </div>
      </section>

      <section className="section">
        <div className="container-custom">
          {isLoading ? (
            <div className="text-center py-12">
              <p className="text-lg text-gray-600">Chargement...</p>
            </div>
          ) : data?.data.trainings && data.data.trainings.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {data.data.trainings.map((training) => (
                <div key={training.id} className="card p-6">
                  <div className="mb-4">
                    <span className="inline-block px-3 py-1 bg-primary-100 text-primary-700 rounded-full text-sm font-medium">
                      {training.level}
                    </span>
                  </div>

                  <h3 className="text-xl font-bold text-primary-800 mb-2">{training.title}</h3>

                  <p className="text-gray-600 mb-4 line-clamp-3">{training.short_description}</p>

                  <div className="space-y-2 mb-6">
                    <div className="flex justify-between text-sm">
                      <span className="text-gray-600">Durée:</span>
                      <span className="font-medium">{training.duration}h</span>
                    </div>
                    <div className="flex justify-between text-sm">
                      <span className="text-gray-600">Prix:</span>
                      <span className="font-medium text-primary-600">{training.price}€</span>
                    </div>
                    <div className="flex justify-between text-sm">
                      <span className="text-gray-600">Participants max:</span>
                      <span className="font-medium">{training.max_participants}</span>
                    </div>
                  </div>

                  <button className="btn-primary w-full">S'inscrire</button>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-12">
              <p className="text-lg text-gray-600">Aucune formation disponible pour le moment</p>
            </div>
          )}
        </div>
      </section>
    </div>
  )
}

export default TrainingsPage
