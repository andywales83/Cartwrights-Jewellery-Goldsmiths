"""
URL path for the user reviews
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('add_review/', views.add_review, name='add_review'),
    path('edit_review/<slug:slug>/',
         views.edit_review, name='edit_review'),
    path('delete_review/<slug:slug>/',
         views.delete_review, name='delete_review'),
    path('<slug:slug>/', views.review_details, name='review_details'),
]
