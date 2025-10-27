from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.models import db, Training, TrainingSession
from app.utils.decorators import admin_required


class TrainingListResource(Resource):
    """Liste des formations"""

    def get(self):
        trainings = Training.query.filter_by(active=True).all()
        return {
            'trainings': [t.to_dict(include_sessions=True) for t in trainings]
        }, 200

    @jwt_required()
    @admin_required
    def post(self):
        data = request.get_json()
        training = Training(**data)
        db.session.add(training)
        db.session.commit()
        return {'training': training.to_dict()}, 201


class TrainingDetailResource(Resource):
    """Détail d'une formation"""

    def get(self, training_id):
        training = Training.query.get_or_404(training_id)
        return training.to_dict(include_sessions=True), 200


class TrainingSessionResource(Resource):
    """Sessions de formation"""

    def get(self, training_id):
        sessions = TrainingSession.query.filter_by(
            training_id=training_id, active=True
        ).all()
        return {'sessions': [s.to_dict() for s in sessions]}, 200
