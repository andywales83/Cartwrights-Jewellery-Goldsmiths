"""
URL path for the user reviews
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('<slug:slug>/', views.review_details, name='review_details'),
]
