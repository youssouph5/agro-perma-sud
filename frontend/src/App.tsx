import { Routes, Route } from 'react-router-dom'
import Navbar from '@components/Navbar/Navbar'
import Footer from '@components/Footer/Footer'
import HomePage from '@pages/HomePage'
import PresentationPage from '@pages/PresentationPage'
import ServicesPage from '@pages/ServicesPage'
import ProjectsPage from '@pages/ProjectsPage'
import TrainingsPage from '@pages/TrainingsPage'
import ContactPage from '@pages/ContactPage'

function App() {
  return (
    <div className="min-h-screen flex flex-col bg-white">
      <Navbar />
      <main className="flex-grow">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/presentation" element={<PresentationPage />} />
          <Route path="/services" element={<ServicesPage />} />
          <Route path="/realisations" element={<ProjectsPage />} />
          <Route path="/formations" element={<TrainingsPage />} />
          <Route path="/contact" element={<ContactPage />} />
        </Routes>
      </main>
      <Footer />
    </div>
  )
}

export default App
