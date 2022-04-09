"""
User review model
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    """ a view to add a post to the blog """

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            author = request.user
            obj.author = author
            obj.save()

            messages.success(request, "Successfully added your user review")
            return redirect(reverse('review_details', args=[obj.slug]))
        else:
            messages.error(
                request, "Failed to add your user review, please check the form is \
                    valid")
    else:
        form = PostForm()

    template = 'reviews/add_review.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)
