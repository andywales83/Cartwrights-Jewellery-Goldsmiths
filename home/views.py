"""
Views for Home App
"""
from django.shortcuts import render

# Create your views here.


def index(request):
    """
    A view that returns the main index page for the user
    """

    return render(request, 'home/index.html')
