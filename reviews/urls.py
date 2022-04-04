"""
URL path for the user reviews
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
]
