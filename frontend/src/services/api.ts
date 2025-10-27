import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

// Instance axios configurée
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Intercepteur pour ajouter le token JWT
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Intercepteur pour gérer les erreurs
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // Token expiré, essayer de rafraîchir
      const refreshToken = localStorage.getItem('refresh_token')
      if (refreshToken) {
        try {
          const response = await axios.post(`${API_URL}/auth/refresh`, {
            refresh_token: refreshToken,
          })
          localStorage.setItem('access_token', response.data.access_token)
          // Réessayer la requête originale
          error.config.headers.Authorization = `Bearer ${response.data.access_token}`
          return api.request(error.config)
        } catch (refreshError) {
          // Échec du refresh, déconnecter l'utilisateur
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
          window.location.href = '/login'
        }
      }
    }
    return Promise.reject(error)
  }
)

export default api

// Types
export interface Project {
  id: number
  title: string
  slug: string
  description: string
  short_description: string
  location: string
  start_date: string
  end_date?: string
  status: string
  featured: boolean
  surface_area?: number
  techniques_used?: string[]
  published: boolean
  media?: Media[]
}

export interface Training {
  id: number
  title: string
  slug: string
  description: string
  short_description: string
  level: string
  duration: number
  max_participants: number
  price: number
  prerequisites?: string
  objectives?: string[]
  program?: any
  certification: boolean
  active: boolean
  sessions?: TrainingSession[]
}

export interface TrainingSession {
  id: number
  training_id: number
  start_date: string
  end_date: string
  location: string
  instructor: string
  available_spots: number
  remaining_spots: number
  is_full: boolean
  status: string
}

export interface Visit {
  id: number
  type: string
  title: string
  description: string
  duration: number
  max_participants: number
  price_per_person: number
  includes?: string[]
  meeting_point: string
  active: boolean
}

export interface Media {
  id: number
  filename: string
  file_url: string
  media_type: string
  title?: string
  description?: string
  alt_text?: string
}

export interface User {
  id: number
  email: string
  first_name?: string
  last_name?: string
  role: string
}

export interface LoginCredentials {
  email: string
  password: string
}

export interface RegisterData {
  email: string
  password: string
  first_name?: string
  last_name?: string
  phone?: string
}

// Services API
export const authService = {
  login: (credentials: LoginCredentials) => api.post('/auth/login', credentials),
  register: (data: RegisterData) => api.post('/auth/register', data),
  logout: () => {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
  },
}

export const projectsService = {
  getAll: (params?: any) => api.get<{ projects: Project[] }>('/projects', { params }),
  getOne: (id: number) => api.get<Project>(`/projects/${id}`),
  create: (data: Partial<Project>) => api.post('/projects', data),
  update: (id: number, data: Partial<Project>) => api.put(`/projects/${id}`, data),
  delete: (id: number) => api.delete(`/projects/${id}`),
}

export const trainingsService = {
  getAll: () => api.get<{ trainings: Training[] }>('/trainings'),
  getOne: (id: number) => api.get<Training>(`/trainings/${id}`),
  getSessions: (id: number) => api.get<{ sessions: TrainingSession[] }>(`/trainings/${id}/sessions`),
}

export const visitsService = {
  getAll: () => api.get<{ visits: Visit[] }>('/visits'),
  getOne: (id: number) => api.get<Visit>(`/visits/${id}`),
  createBooking: (data: any) => api.post('/visits/bookings', data),
}

export const statsService = {
  getGlobalStats: () => api.get('/stats'),
}

export const contactService = {
  sendMessage: (data: { name: string; email: string; subject: string; message: string }) =>
    api.post('/contact', data),
}

export const newsletterService = {
  subscribe: (email: string) => api.post('/newsletter', { email }),
  unsubscribe: (email: string) => api.delete('/newsletter', { data: { email } }),
}
