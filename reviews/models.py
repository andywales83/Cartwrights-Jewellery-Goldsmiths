"""
New User Review Model
"""
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    The model for a new review post
    """
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_review", default=1)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        To show most recent news posts first
        """
        ordering = ['-created_on']


class Comment(models.Model):
    """
    The model for a comment on a user review
    """
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ to show most recent comments first """
        ordering = ['-created_on']
