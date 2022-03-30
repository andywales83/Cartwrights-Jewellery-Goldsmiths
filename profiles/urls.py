""" url path for the user profile """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
]
