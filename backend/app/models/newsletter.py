from datetime import datetime
from . import db


class NewsletterSubscriber(db.Model):
    """Modèle Abonné Newsletter"""
    __tablename__ = 'newsletter_subscribers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    interests = db.Column(db.JSON)  # Liste des centres d'intérêt
    status = db.Column(db.String(50), default='active')  # active, unsubscribed, bounced
    source = db.Column(db.String(100))  # D'où vient l'inscription
    confirmed = db.Column(db.Boolean, default=False)
    confirmation_token = db.Column(db.String(200))
    mailchimp_id = db.Column(db.String(200))  # ID dans Mailchimp
    subscribed_at = db.Column(db.DateTime, default=datetime.utcnow)
    unsubscribed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def is_active(self):
        """Propriété pour vérifier si l'abonnement est actif"""
        return self.status == 'active'

    def to_dict(self):
        """Convertir en dictionnaire"""
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'interests': self.interests,
            'status': self.status,
            'is_active': self.is_active,
            'confirmed': self.confirmed,
            'subscribed_at': self.subscribed_at.isoformat() if self.subscribed_at else None
        }

    def __repr__(self):
        return f'<NewsletterSubscriber {self.email}>'


class Campaign(db.Model):
    """Modèle Campagne d'emailing"""
    __tablename__ = 'campaigns'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    content_html = db.Column(db.Text)
    content_text = db.Column(db.Text)
    status = db.Column(db.String(50), default='draft')  # draft, scheduled, sent, cancelled
    segment = db.Column(db.JSON)  # Critères de segmentation
    scheduled_at = db.Column(db.DateTime)
    sent_at = db.Column(db.DateTime)

    # Statistiques
    recipients_count = db.Column(db.Integer, default=0)
    opened_count = db.Column(db.Integer, default=0)
    clicked_count = db.Column(db.Integer, default=0)
    bounced_count = db.Column(db.Integer, default=0)
    unsubscribed_count = db.Column(db.Integer, default=0)

    mailchimp_campaign_id = db.Column(db.String(200))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def open_rate(self):
        """Taux d'ouverture"""
        if self.recipients_count == 0:
            return 0
        return round((self.opened_count / self.recipients_count) * 100, 2)

    @property
    def click_rate(self):
        """Taux de clic"""
        if self.recipients_count == 0:
            return 0
        return round((self.clicked_count / self.recipients_count) * 100, 2)

    def to_dict(self):
        """Convertir en dictionnaire"""
        return {
            'id': self.id,
            'title': self.title,
            'subject': self.subject,
            'status': self.status,
            'scheduled_at': self.scheduled_at.isoformat() if self.scheduled_at else None,
            'sent_at': self.sent_at.isoformat() if self.sent_at else None,
            'recipients_count': self.recipients_count,
            'opened_count': self.opened_count,
            'clicked_count': self.clicked_count,
            'open_rate': self.open_rate,
            'click_rate': self.click_rate,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<Campaign {self.title}>'
