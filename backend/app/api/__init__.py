from flask import Blueprint
from flask_restful import Api

# Création des blueprints
api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

# Import des resources
from .auth import LoginResource, RegisterResource, RefreshTokenResource
from .projects import ProjectListResource, ProjectDetailResource
from .trainings import TrainingListResource, TrainingDetailResource, TrainingSessionResource
from .visits import VisitListResource, VisitDetailResource, VisitBookingResource
from .media import MediaUploadResource, MediaDetailResource
from .stats import StatsResource
from .contact import ContactResource, NewsletterResource

# Enregistrement des routes

# Auth
api.add_resource(RegisterResource, '/auth/register')
api.add_resource(LoginResource, '/auth/login')
api.add_resource(RefreshTokenResource, '/auth/refresh')

# Projets
api.add_resource(ProjectListResource, '/projects')
api.add_resource(ProjectDetailResource, '/projects/<int:project_id>')

# Formations
api.add_resource(TrainingListResource, '/trainings')
api.add_resource(TrainingDetailResource, '/trainings/<int:training_id>')
api.add_resource(TrainingSessionResource, '/trainings/<int:training_id>/sessions')

# Visites
api.add_resource(VisitListResource, '/visits')
api.add_resource(VisitDetailResource, '/visits/<int:visit_id>')
api.add_resource(VisitBookingResource, '/visits/bookings')

# Médias
api.add_resource(MediaUploadResource, '/media/upload')
api.add_resource(MediaDetailResource, '/media/<int:media_id>')

# Statistiques
api.add_resource(StatsResource, '/stats')

# Contact et Newsletter
api.add_resource(ContactResource, '/contact')
api.add_resource(NewsletterResource, '/newsletter')

__all__ = ['api_bp']
