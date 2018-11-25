from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		exclude = ['pub_date', 'is_visible']