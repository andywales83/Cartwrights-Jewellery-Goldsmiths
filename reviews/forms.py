"""
User comments model
"""
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    Model for a user to create a comment
    """
    class Meta:
        """
        Comment fields
        """
        model = Comment
        fields = ('name', 'comment_body')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment_body'].label = "Comment"
