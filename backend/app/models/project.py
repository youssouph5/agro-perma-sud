from datetime import datetime
from enum import Enum
from . import db


class ProjectStatus(str, Enum):
    """Statuts de projet"""
    PLANNING = 'planning'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    ARCHIVED = 'archived'


class Project(db.Model):
    """Modèle Projet/Réalisation"""
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(250), unique=True, index=True)
    description = db.Column(db.Text)
    short_description = db.Column(db.String(500))
    location = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.Enum(ProjectStatus), default=ProjectStatus.PLANNING)
    featured = db.Column(db.Boolean, default=False)
    surface_area = db.Column(db.Float)  # Surface en m²
    budget = db.Column(db.Numeric(10, 2))
    techniques_used = db.Column(db.JSON)  # Liste des techniques de permaculture
    results = db.Column(db.Text)
    lessons_learned = db.Column(db.Text)
    published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relations
    media_files = db.relationship('Media', backref='project', lazy='dynamic',
                                  cascade='all, delete-orphan')

    def to_dict(self, include_media=False):
        """Convertir en dictionnaire"""
        data = {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'description': self.description,
            'short_description': self.short_description,
            'location': self.location,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'status': self.status.value if self.status else None,
            'featured': self.featured,
            'surface_area': float(self.surface_area) if self.surface_area else None,
            'budget': float(self.budget) if self.budget else None,
            'techniques_used': self.techniques_used,
            'results': self.results,
            'published': self.published,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

        if include_media:
            data['media'] = [m.to_dict() for m in self.media_files.all()]

        return data

    def __repr__(self):
        return f'<Project {self.title}>'
