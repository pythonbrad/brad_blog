from django import forms
from .models import Article
from .models import Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author', 'pub_date', 'is_visible']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['contains']
