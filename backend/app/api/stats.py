from flask_restful import Resource
from app.models import Project, Training, VisitBooking, NewsletterSubscriber


class StatsResource(Resource):
    """Statistiques globales"""

    def get(self):
        return {
            'total_projects': Project.query.count(),
            'total_trainings': Training.query.count(),
            'total_visits': VisitBooking.query.filter_by(status='confirmed').count(),
            'total_subscribers': NewsletterSubscriber.query.filter_by(status='active').count()
        }, 200
