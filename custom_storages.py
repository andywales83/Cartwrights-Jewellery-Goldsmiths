"""
Custom storage setup for the Media & Static Files
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Custom Staticfiles setup
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Custom Mediafiles setup
    """
    location = settings.MEDIAFILES_LOCATION
