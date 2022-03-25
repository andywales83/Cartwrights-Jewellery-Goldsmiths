""" url path for the home App """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
]
