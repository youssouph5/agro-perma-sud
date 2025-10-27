from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app.models import User


def admin_required(fn):
    """Décorateur pour vérifier les droits admin"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if not user or user.role != 'admin':
            return jsonify({'error': 'Accès non autorisé'}), 403

        return fn(*args, **kwargs)

    return wrapper
