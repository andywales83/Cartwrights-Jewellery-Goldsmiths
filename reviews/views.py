"""
User review model
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from .models import Post

from .forms import CommentForm, PostForm


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


@login_required
def add_review(request):
    """
    Add a new user review
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added your review!')
            return redirect(reverse('review_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add your review. Please \
                ensure the form is valid.')
    else:
        form = PostForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
