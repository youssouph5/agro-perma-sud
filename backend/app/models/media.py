from datetime import datetime
from enum import Enum
from . import db


class MediaType(str, Enum):
    """Types de média"""
    IMAGE = 'image'
    VIDEO = 'video'
    DOCUMENT = 'document'
    AUDIO = 'audio'


class Media(db.Model):
    """Modèle Média"""
    __tablename__ = 'media'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255))
    file_path = db.Column(db.String(500))  # Chemin local ou URL S3
    file_url = db.Column(db.String(500))  # URL publique
    file_size = db.Column(db.Integer)  # Taille en bytes
    mime_type = db.Column(db.String(100))
    media_type = db.Column(db.Enum(MediaType), nullable=False)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    alt_text = db.Column(db.String(200))  # Pour l'accessibilité
    width = db.Column(db.Integer)  # Pour les images
    height = db.Column(db.Integer)  # Pour les images
    duration = db.Column(db.Integer)  # Pour vidéos/audio en secondes

    # Relations polymorphes
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    training_id = db.Column(db.Integer, db.ForeignKey('trainings.id'))

    # Métadonnées
    featured = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)
    tags = db.Column(db.JSON)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """Convertir en dictionnaire"""
        return {
            'id': self.id,
            'filename': self.filename,
            'original_filename': self.original_filename,
            'file_url': self.file_url,
            'file_size': self.file_size,
            'mime_type': self.mime_type,
            'media_type': self.media_type.value if self.media_type else None,
            'title': self.title,
            'description': self.description,
            'alt_text': self.alt_text,
            'width': self.width,
            'height': self.height,
            'duration': self.duration,
            'featured': self.featured,
            'tags': self.tags,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<Media {self.filename}>'
