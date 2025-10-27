import re
from email_validator import validate_email as ev_validate_email, EmailNotValidError


def validate_email(email):
    """Valider une adresse email"""
    try:
        ev_validate_email(email)
        return True
    except EmailNotValidError:
        return False


def validate_phone(phone):
    """Valider un numéro de téléphone"""
    pattern = r'^(\+33|0)[1-9](\d{8})$'
    return bool(re.match(pattern, phone.replace(' ', '')))


def validate_password(password):
    """Valider un mot de passe (min 8 caractères)"""
    return len(password) >= 8
