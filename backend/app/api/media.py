from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.models import db, Media
from app.utils.decorators import admin_required


class MediaUploadResource(Resource):
    @jwt_required()
    @admin_required
    def post(self):
        # Logique d'upload de média
        return {'message': 'Upload média'}, 201


class MediaDetailResource(Resource):
    def get(self, media_id):
        media = Media.query.get_or_404(media_id)
        return media.to_dict(), 200
