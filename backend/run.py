import os
from app import create_app, db
from app.models import User, Project, Training, Visit, Media

# Créer l'application
app = create_app(os.getenv('FLASK_ENV') or 'default')


@app.shell_context_processor
def make_shell_context():
    """Contexte pour le shell Flask"""
    return {
        'db': db,
        'User': User,
        'Project': Project,
        'Training': Training,
        'Visit': Visit,
        'Media': Media
    }


@app.cli.command()
def init_db():
    """Initialiser la base de données"""
    db.create_all()
    print('Base de données initialisée.')


@app.cli.command()
def seed_db():
    """Ajouter des données de test"""
    # Créer un utilisateur admin
    admin = User(
        email='admin@agriculture-permaculture.com',
        first_name='Admin',
        last_name='Système',
        role='admin'
    )
    admin.set_password('admin123')

    db.session.add(admin)
    db.session.commit()

    print('Données de test ajoutées.')


if __name__ == '__main__':
    # Utiliser use_reloader=True avec use_debugger pour un meilleur contrôle
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=True,
        use_debugger=True
    )
