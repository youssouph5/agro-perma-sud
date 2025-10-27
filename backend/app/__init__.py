from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import config
from app.models import db
from app.services.email_service import mail


migrate = Migrate()
jwt = JWTManager()


def create_app(config_name='default'):
    """Factory pour créer l'application Flask"""
    app = Flask(__name__)

    # Charger la configuration
    app.config.from_object(config[config_name])

    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Enregistrer les blueprints
    from app.api import api_bp
    app.register_blueprint(api_bp)

    # Routes de santé
    @app.route('/health')
    def health():
        return {'status': 'healthy'}, 200

    @app.route('/')
    def index():
        return {
            'message': 'API Agroécologie & Permaculture',
            'version': '1.0',
            'endpoints': {
                'auth': '/api/auth',
                'projects': '/api/projects',
                'trainings': '/api/trainings',
                'visits': '/api/visits',
                'stats': '/api/stats'
            }
        }, 200

    # Gestionnaire d'erreurs global
    @app.errorhandler(Exception)
    def handle_exception(e):
        """Gestionnaire d'erreurs global pour éviter les crashs"""
        import traceback
        app.logger.error(f"Erreur non gérée: {str(e)}")
        app.logger.error(traceback.format_exc())
        return {
            'error': 'Une erreur interne est survenue',
            'message': str(e) if app.debug else 'Erreur serveur'
        }, 500

    return app
