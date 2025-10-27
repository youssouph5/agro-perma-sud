from slugify import slugify
from datetime import datetime
import uuid


def generate_slug(text):
    """Générer un slug à partir d'un texte"""
    return slugify(text)


def generate_confirmation_code():
    """Générer un code de confirmation unique"""
    return str(uuid.uuid4())[:8].upper()


def format_price(amount):
    """Formater un prix"""
    return f"{float(amount):.2f} €"


def parse_date(date_string):
    """Parser une date"""
    try:
        return datetime.fromisoformat(date_string)
    except:
        return None
