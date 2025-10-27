import os
from werkzeug.utils import secure_filename
from PIL import Image
import boto3
from flask import current_app


class MediaService:
    """Service de gestion des médias"""

    @staticmethod
    def allowed_file(filename):
        """Vérifier si le fichier est autorisé"""
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

    @classmethod
    def save_file(cls, file, folder='uploads'):
        """Sauvegarder un fichier localement"""
        if not cls.allowed_file(file.filename):
            raise ValueError('Type de fichier non autorisé')

        filename = secure_filename(file.filename)
        upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], folder)

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)

        return filepath

    @classmethod
    def resize_image(cls, image_path, max_width=1920, max_height=1080):
        """Redimensionner une image"""
        img = Image.open(image_path)

        if img.width > max_width or img.height > max_height:
            img.thumbnail((max_width, max_height), Image.LANCZOS)
            img.save(image_path, optimize=True, quality=85)

        return img.width, img.height

    @classmethod
    def upload_to_s3(cls, file, bucket_name, key):
        """Upload vers AWS S3"""
        s3_client = boto3.client(
            's3',
            aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
            region_name=current_app.config['AWS_REGION']
        )

        s3_client.upload_fileobj(
            file,
            bucket_name,
            key,
            ExtraArgs={'ACL': 'public-read'}
        )

        url = f"https://{bucket_name}.s3.{current_app.config['AWS_REGION']}.amazonaws.com/{key}"
        return url

    @classmethod
    def delete_from_s3(cls, bucket_name, key):
        """Supprimer de S3"""
        s3_client = boto3.client(
            's3',
            aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY']
        )

        s3_client.delete_object(Bucket=bucket_name, Key=key)
