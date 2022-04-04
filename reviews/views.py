"""
User review model
"""
from django.shortcuts import render
from .models import Post


def reviews(request):
    """
    Display all user review posts
    """
    posts = Post.objects.all()
    template = 'reviews/reviews.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)
