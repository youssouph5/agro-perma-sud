from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.models import db, User
from app.utils.validators import validate_email


class RegisterResource(Resource):
    """Inscription utilisateur"""

    def post(self):
        data = request.get_json()

        # Validation
        if not data or not data.get('email') or not data.get('password'):
            return {'error': 'Email et mot de passe requis'}, 400

        email = data['email'].lower().strip()
        if not validate_email(email):
            return {'error': 'Email invalide'}, 400

        # Vérifier si l'utilisateur existe déjà
        if User.query.filter_by(email=email).first():
            return {'error': 'Cet email est déjà utilisé'}, 400

        # Créer l'utilisateur
        user = User(
            email=email,
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            phone=data.get('phone')
        )
        user.set_password(data['password'])

        try:
            db.session.add(user)
            db.session.commit()

            # Générer les tokens
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)

            return {
                'message': 'Utilisateur créé avec succès',
                'user': user.to_dict(),
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 201

        except Exception as e:
            db.session.rollback()
            return {'error': f'Erreur lors de la création: {str(e)}'}, 500


class LoginResource(Resource):
    """Connexion utilisateur"""

    def post(self):
        data = request.get_json()

        if not data or not data.get('email') or not data.get('password'):
            return {'error': 'Email et mot de passe requis'}, 400

        email = data['email'].lower().strip()
        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(data['password']):
            return {'error': 'Email ou mot de passe incorrect'}, 401

        if not user.is_active:
            return {'error': 'Compte désactivé'}, 403

        # Générer les tokens
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return {
            'message': 'Connexion réussie',
            'user': user.to_dict(),
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200


class RefreshTokenResource(Resource):
    """Rafraîchir le token d'accès"""

    @jwt_required(refresh=True)
    def post(self):
        current_user_id = get_jwt_identity()
        access_token = create_access_token(identity=current_user_id)

        return {'access_token': access_token}, 200
