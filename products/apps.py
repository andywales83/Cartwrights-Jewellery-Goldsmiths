"""
Products Config class
"""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Products config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
