"""
User review model
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post

from .forms import CommentForm


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


def review_details(request, slug):
    """
    Displays the full user review & any comments
    """
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            messages.success(request, "Successfully added your comment")
            return redirect('review_details', slug=post.slug)
        else:
            messages.error(
                request, "Failed to add comment, please check the form is \
                    valid")
    else:
        form = CommentForm()

    template = 'reviews/review_details.html'
    context = {
        'post': post,
        'form': form
    }

    return render(request, template, context)
