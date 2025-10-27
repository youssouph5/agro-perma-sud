import stripe
from flask import current_app


class PaymentService:
    """Service de paiement Stripe"""

    @staticmethod
    def init_stripe():
        """Initialiser Stripe"""
        stripe.api_key = current_app.config['STRIPE_SECRET_KEY']

    @classmethod
    def create_payment_intent(cls, amount, currency='eur', metadata=None):
        """Créer une intention de paiement"""
        cls.init_stripe()

        intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Convertir en centimes
            currency=currency,
            metadata=metadata or {}
        )

        return intent

    @classmethod
    def create_checkout_session(cls, items, success_url, cancel_url, metadata=None):
        """Créer une session de paiement"""
        cls.init_stripe()

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
            metadata=metadata or {}
        )

        return session

    @classmethod
    def verify_webhook(cls, payload, sig_header):
        """Vérifier un webhook Stripe"""
        cls.init_stripe()

        try:
            event = stripe.Webhook.construct_event(
                payload,
                sig_header,
                current_app.config['STRIPE_WEBHOOK_SECRET']
            )
            return event
        except Exception as e:
            raise ValueError(f'Webhook invalide: {str(e)}')

    @classmethod
    def refund_payment(cls, payment_intent_id, amount=None):
        """Rembourser un paiement"""
        cls.init_stripe()

        refund = stripe.Refund.create(
            payment_intent=payment_intent_id,
            amount=int(amount * 100) if amount else None
        )

        return refund
