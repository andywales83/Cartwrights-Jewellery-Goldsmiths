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


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-product-form-field'
