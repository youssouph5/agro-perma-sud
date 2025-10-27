from datetime import datetime
from enum import Enum
from . import db


class TrainingLevel(str, Enum):
    """Niveaux de formation"""
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    EXPERT = 'expert'


class Training(db.Model):
    """Modèle Formation"""
    __tablename__ = 'trainings'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(250), unique=True, index=True)
    description = db.Column(db.Text)
    short_description = db.Column(db.String(500))
    level = db.Column(db.Enum(TrainingLevel), default=TrainingLevel.BEGINNER)
    duration = db.Column(db.Integer)  # Durée en heures
    max_participants = db.Column(db.Integer, default=15)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    prerequisites = db.Column(db.Text)
    objectives = db.Column(db.JSON)  # Liste des objectifs pédagogiques
    program = db.Column(db.JSON)  # Programme détaillé
    materials_provided = db.Column(db.JSON)  # Supports fournis
    materials_needed = db.Column(db.JSON)  # Matériel à apporter
    certification = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)
    category = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relations
    sessions = db.relationship('TrainingSession', backref='training', lazy='dynamic',
                               cascade='all, delete-orphan')
    media_files = db.relationship('Media', backref='training', lazy='dynamic')

    def to_dict(self, include_sessions=False):
        """Convertir en dictionnaire"""
        data = {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'description': self.description,
            'short_description': self.short_description,
            'level': self.level.value if self.level else None,
            'duration': self.duration,
            'max_participants': self.max_participants,
            'price': float(self.price) if self.price else None,
            'prerequisites': self.prerequisites,
            'objectives': self.objectives,
            'program': self.program,
            'materials_provided': self.materials_provided,
            'materials_needed': self.materials_needed,
            'certification': self.certification,
            'active': self.active,
            'category': self.category,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

        if include_sessions:
            data['sessions'] = [s.to_dict() for s in self.sessions.filter_by(active=True).all()]

        return data

    def __repr__(self):
        return f'<Training {self.title}>'


class TrainingSession(db.Model):
    """Modèle Session de formation"""
    __tablename__ = 'training_sessions'

    id = db.Column(db.Integer, primary_key=True)
    training_id = db.Column(db.Integer, db.ForeignKey('trainings.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200))
    instructor = db.Column(db.String(100))
    available_spots = db.Column(db.Integer)
    status = db.Column(db.String(50), default='scheduled')  # scheduled, confirmed, completed, cancelled
    notes = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relations
    bookings = db.relationship('Booking', backref='training_session', lazy='dynamic')

    @property
    def is_full(self):
        """Vérifier si la session est complète"""
        if not self.available_spots:
            return False
        confirmed_bookings = self.bookings.filter_by(status='confirmed').count()
        return confirmed_bookings >= self.available_spots

    @property
    def remaining_spots(self):
        """Nombre de places restantes"""
        if not self.available_spots:
            return 0
        confirmed_bookings = self.bookings.filter_by(status='confirmed').count()
        return max(0, self.available_spots - confirmed_bookings)

    def to_dict(self):
        """Convertir en dictionnaire"""
        return {
            'id': self.id,
            'training_id': self.training_id,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'location': self.location,
            'instructor': self.instructor,
            'available_spots': self.available_spots,
            'remaining_spots': self.remaining_spots,
            'is_full': self.is_full,
            'status': self.status,
            'active': self.active
        }

    def __repr__(self):
        return f'<TrainingSession {self.id} - {self.training.title}>'
