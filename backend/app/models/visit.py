from datetime import datetime
from . import db


class Visit(db.Model):
    """Modèle Type de visite"""
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)  # découverte, technique, saisonnière
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    duration = db.Column(db.Integer)  # Durée en minutes
    max_participants = db.Column(db.Integer, default=10)
    price_per_person = db.Column(db.Numeric(10, 2), nullable=False)
    includes = db.Column(db.JSON)  # Ce qui est inclus
    meeting_point = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relations
    bookings = db.relationship('VisitBooking', backref='visit', lazy='dynamic')

    def to_dict(self):
        """Convertir en dictionnaire"""
        return {
            'id': self.id,
            'type': self.type,
            'title': self.title,
            'description': self.description,
            'duration': self.duration,
            'max_participants': self.max_participants,
            'price_per_person': float(self.price_per_person) if self.price_per_person else None,
            'includes': self.includes,
            'meeting_point': self.meeting_point,
            'active': self.active
        }

    def __repr__(self):
        return f'<Visit {self.title}>'


class VisitBooking(db.Model):
    """Modèle Réservation de visite"""
    __tablename__ = 'visit_bookings'

    id = db.Column(db.Integer, primary_key=True)
    visit_id = db.Column(db.Integer, db.ForeignKey('visits.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    visit_date = db.Column(db.DateTime, nullable=False)
    participants = db.Column(db.Integer, default=1)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, confirmed, completed, cancelled
    payment_status = db.Column(db.String(50), default='pending')
    payment_id = db.Column(db.String(200))  # ID transaction Stripe
    special_requests = db.Column(db.Text)
    confirmation_code = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """Convertir en dictionnaire"""
        return {
            'id': self.id,
            'visit': self.visit.to_dict() if self.visit else None,
            'visit_date': self.visit_date.isoformat() if self.visit_date else None,
            'participants': self.participants,
            'total_price': float(self.total_price) if self.total_price else None,
            'status': self.status,
            'payment_status': self.payment_status,
            'confirmation_code': self.confirmation_code,
            'special_requests': self.special_requests,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<VisitBooking {self.id} - {self.confirmation_code}>'


class Booking(db.Model):
    """Modèle Réservation générique (formations)"""
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    bookable_type = db.Column(db.String(50))  # 'training' ou 'visit'
    training_session_id = db.Column(db.Integer, db.ForeignKey('training_sessions.id'))
    participants = db.Column(db.Integer, default=1)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(50), default='pending')
    payment_status = db.Column(db.String(50), default='pending')
    payment_id = db.Column(db.String(200))
    confirmation_code = db.Column(db.String(50), unique=True)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """Convertir en dictionnaire"""
        return {
            'id': self.id,
            'bookable_type': self.bookable_type,
            'participants': self.participants,
            'total_price': float(self.total_price) if self.total_price else None,
            'status': self.status,
            'payment_status': self.payment_status,
            'confirmation_code': self.confirmation_code,
            'session': self.training_session.to_dict() if self.training_session else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<Booking {self.id} - {self.confirmation_code}>'
