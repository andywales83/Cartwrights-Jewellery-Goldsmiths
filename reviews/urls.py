"""
URL path for the user reviews
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('detail/<slug:slug>/', views.review_details, name='review_details'),
    path('add_review/', views.add_review, name='add_review'),
]
