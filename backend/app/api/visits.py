from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Visit, VisitBooking
import uuid


class VisitListResource(Resource):
    def get(self):
        visits = Visit.query.filter_by(active=True).all()
        return {'visits': [v.to_dict() for v in visits]}, 200


class VisitDetailResource(Resource):
    def get(self, visit_id):
        visit = Visit.query.get_or_404(visit_id)
        return visit.to_dict(), 200


class VisitBookingResource(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()

        booking = VisitBooking(
            visit_id=data['visit_id'],
            user_id=user_id,
            visit_date=data['visit_date'],
            participants=data['participants'],
            total_price=data['total_price'],
            confirmation_code=str(uuid.uuid4())[:8].upper()
        )
        db.session.add(booking)
        db.session.commit()
        return {'booking': booking.to_dict()}, 201
