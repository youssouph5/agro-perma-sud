from flask import current_app, render_template
from flask_mail import Message, Mail

mail = Mail()


class EmailService:
    """Service d'envoi d'emails"""

    @staticmethod
    def send_email(to, subject, template, **kwargs):
        """Envoyer un email"""
        msg = Message(
            subject,
            recipients=[to] if isinstance(to, str) else to,
            sender=current_app.config['MAIL_DEFAULT_SENDER']
        )

        try:
            msg.html = render_template(f'emails/{template}.html', **kwargs)
            msg.body = render_template(f'emails/{template}.txt', **kwargs)
        except:
            # Fallback si pas de template
            msg.html = kwargs.get('html', '')
            msg.body = kwargs.get('text', '')

        mail.send(msg)

    @classmethod
    def send_booking_confirmation(cls, booking, user):
        """Email de confirmation de réservation"""
        cls.send_email(
            to=user.email,
            subject='Confirmation de réservation',
            template='booking_confirmation',
            booking=booking,
            user=user
        )

    @classmethod
    def send_welcome_email(cls, user):
        """Email de bienvenue"""
        cls.send_email(
            to=user.email,
            subject='Bienvenue sur Agroécologie & Permaculture',
            template='welcome',
            user=user
        )

    @classmethod
    def send_newsletter(cls, subscribers, campaign):
        """Envoyer une newsletter"""
        for subscriber in subscribers:
            cls.send_email(
                to=subscriber.email,
                subject=campaign.subject,
                template='newsletter',
                content=campaign.content_html,
                subscriber=subscriber
            )

    @classmethod
    def send_contact_notification(cls, name, email, subject, message):
        """Envoyer une notification pour un message de contact"""
        admin_email = current_app.config.get('ADMIN_EMAIL', 'admin@agriculture.com')
        cls.send_email(
            to=admin_email,
            subject=f'Nouveau message de contact: {subject}',
            template='contact_notification',
            html=f'''
                <h2>Nouveau message de contact</h2>
                <p><strong>De:</strong> {name} ({email})</p>
                <p><strong>Sujet:</strong> {subject}</p>
                <p><strong>Message:</strong></p>
                <p>{message}</p>
            ''',
            text=f'''
                Nouveau message de contact
                De: {name} ({email})
                Sujet: {subject}
                Message: {message}
            '''
        )

    @classmethod
    def send_newsletter_welcome(cls, email):
        """Envoyer un email de bienvenue pour la newsletter"""
        cls.send_email(
            to=email,
            subject='Bienvenue à notre newsletter - Agroécologie & Permaculture',
            template='newsletter_welcome',
            html=f'''
                <h2>Bienvenue à notre newsletter!</h2>
                <p>Merci de vous être inscrit à notre newsletter.</p>
                <p>Vous recevrez régulièrement nos actualités, conseils et informations sur nos formations et projets.</p>
                <p>À bientôt!</p>
                <p>L'équipe Agroécologie & Permaculture</p>
            ''',
            text=f'''
                Bienvenue à notre newsletter!

                Merci de vous être inscrit à notre newsletter.
                Vous recevrez régulièrement nos actualités, conseils et informations sur nos formations et projets.

                À bientôt!
                L'équipe Agroécologie & Permaculture
            '''
        )
