from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import des modèles pour les rendre disponibles
from .user import User
from .project import Project, ProjectStatus
from .training import Training, TrainingLevel, TrainingSession
from .visit import Visit, VisitBooking
from .media import Media, MediaType
from .newsletter import NewsletterSubscriber, Campaign

__all__ = [
    'db',
    'User',
    'Project',
    'ProjectStatus',
    'Training',
    'TrainingLevel',
    'TrainingSession',
    'Visit',
    'VisitBooking',
    'Media',
    'MediaType',
    'NewsletterSubscriber',
    'Campaign'
]
