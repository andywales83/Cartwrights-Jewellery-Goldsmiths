"""
Configure Basket application
"""
from django.apps import AppConfig


class BasketConfig(AppConfig):
    """
    Cart Basket Configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
