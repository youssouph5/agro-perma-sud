from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Project, User
from app.utils.decorators import admin_required
from sqlalchemy import or_


class ProjectListResource(Resource):
    """Liste des projets/réalisations"""

    def get(self):
        """Récupérer la liste des projets"""
        # Paramètres de filtrage
        featured = request.args.get('featured', type=bool)
        status = request.args.get('status')
        search = request.args.get('search')
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 12, type=int)

        # Construction de la requête
        query = Project.query.filter_by(published=True)

        if featured is not None:
            query = query.filter_by(featured=featured)

        if status:
            query = query.filter_by(status=status)

        if search:
            search_filter = f'%{search}%'
            query = query.filter(
                or_(
                    Project.title.ilike(search_filter),
                    Project.description.ilike(search_filter),
                    Project.location.ilike(search_filter)
                )
            )

        # Pagination
        query = query.order_by(Project.created_at.desc())
        paginated = query.paginate(page=page, per_page=per_page, error_out=False)

        return {
            'projects': [p.to_dict(include_media=True) for p in paginated.items],
            'total': paginated.total,
            'pages': paginated.pages,
            'current_page': page,
            'per_page': per_page
        }, 200

    @jwt_required()
    @admin_required
    def post(self):
        """Créer un nouveau projet"""
        data = request.get_json()

        if not data or not data.get('title'):
            return {'error': 'Titre requis'}, 400

        project = Project(
            title=data['title'],
            slug=data.get('slug'),
            description=data.get('description'),
            short_description=data.get('short_description'),
            location=data.get('location'),
            status=data.get('status', 'planning'),
            featured=data.get('featured', False),
            surface_area=data.get('surface_area'),
            budget=data.get('budget'),
            techniques_used=data.get('techniques_used'),
            results=data.get('results'),
            published=data.get('published', False)
        )

        try:
            db.session.add(project)
            db.session.commit()
            return {
                'message': 'Projet créé avec succès',
                'project': project.to_dict()
            }, 201
        except Exception as e:
            db.session.rollback()
            return {'error': f'Erreur: {str(e)}'}, 500


class ProjectDetailResource(Resource):
    """Détail d'un projet"""

    def get(self, project_id):
        """Récupérer un projet"""
        project = Project.query.get_or_404(project_id)

        if not project.published:
            return {'error': 'Projet non publié'}, 404

        return project.to_dict(include_media=True), 200

    @jwt_required()
    @admin_required
    def put(self, project_id):
        """Mettre à jour un projet"""
        project = Project.query.get_or_404(project_id)
        data = request.get_json()

        # Mise à jour des champs
        for field in ['title', 'slug', 'description', 'short_description', 'location',
                      'status', 'featured', 'surface_area', 'budget', 'techniques_used',
                      'results', 'published']:
            if field in data:
                setattr(project, field, data[field])

        try:
            db.session.commit()
            return {
                'message': 'Projet mis à jour',
                'project': project.to_dict()
            }, 200
        except Exception as e:
            db.session.rollback()
            return {'error': f'Erreur: {str(e)}'}, 500

    @jwt_required()
    @admin_required
    def delete(self, project_id):
        """Supprimer un projet"""
        project = Project.query.get_or_404(project_id)

        try:
            db.session.delete(project)
            db.session.commit()
            return {'message': 'Projet supprimé'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': f'Erreur: {str(e)}'}, 500
