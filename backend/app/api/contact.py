from flask import request, jsonify
from flask_restful import Resource
from app.models import db, NewsletterSubscriber
from app.services.email_service import EmailService
from datetime import datetime

class ContactResource(Resource):
    """Endpoint pour les messages de contact"""

    def post(self):
        try:
            data = request.get_json()

            # Validation
            required_fields = ['name', 'email', 'subject', 'message']
            for field in required_fields:
                if not data.get(field):
                    return {'error': f'Le champ {field} est requis'}, 400

            # Envoyer email à l'équipe (désactivé en dev)
            # email_service = EmailService()
            # email_service.send_contact_notification(
            #     name=data['name'],
            #     email=data['email'],
            #     subject=data['subject'],
            #     message=data['message']
            # )
            print(f"Contact reçu de {data['name']} ({data['email']}): {data['subject']}")

            return {
                'message': 'Votre message a été envoyé avec succès. Nous vous répondrons dans les plus brefs délais.'
            }, 200

        except Exception as e:
            return {'error': str(e)}, 500


class NewsletterResource(Resource):
    """Endpoint pour l'inscription à la newsletter"""

    def post(self):
        try:
            data = request.get_json()

            if not data.get('email'):
                return {'error': 'L\'email est requis'}, 400

            # Vérifier si l'email existe déjà
            existing = NewsletterSubscriber.query.filter_by(email=data['email']).first()
            if existing:
                if existing.status == 'active':
                    return {'message': 'Cet email est déjà inscrit à notre newsletter'}, 200
                else:
                    # Réactiver l'abonnement
                    existing.status = 'active'
                    existing.subscribed_at = datetime.utcnow()
                    existing.unsubscribed_at = None
                    db.session.commit()
                    return {'message': 'Votre abonnement a été réactivé avec succès'}, 200

            # Créer nouvel abonné
            newsletter = NewsletterSubscriber(
                email=data['email']
            )
            db.session.add(newsletter)
            db.session.commit()

            # Envoyer email de bienvenue (désactivé en dev)
            # email_service = EmailService()
            # email_service.send_newsletter_welcome(data['email'])
            print(f"Nouvel abonné à la newsletter: {data['email']}")

            return {
                'message': 'Merci pour votre inscription ! Vous recevrez bientôt nos actualités.'
            }, 201

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500

    def delete(self):
        """Se désabonner de la newsletter"""
        try:
            data = request.get_json()

            if not data.get('email'):
                return {'error': 'L\'email est requis'}, 400

            newsletter = NewsletterSubscriber.query.filter_by(email=data['email']).first()
            if not newsletter:
                return {'error': 'Cet email n\'est pas inscrit'}, 404

            newsletter.status = 'unsubscribed'
            newsletter.unsubscribed_at = datetime.utcnow()
            db.session.commit()

            return {'message': 'Vous avez été désinscrit de notre newsletter'}, 200

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
