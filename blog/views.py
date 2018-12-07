from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from .models import Comment
from .forms import CommentForm

# Create your views here.
def index(request):
	articles = Article.objects.order_by('-pub_date').filter(is_visible=True)
	return render(request, 'blog/index.html', {'articles':articles})

def add(request):
	if request.user.is_staff:
		forms = ArticleForm(request.POST)
		if forms.is_valid():
			article = Article()
			article.title = forms.cleaned_data['title']
			article.author = request.user
			article.contains = forms.cleaned_data['contains']
			article.save()
			return redirect(reverse('index'))
		else:
			return render(request, 'blog/add.html', {'forms':forms})
	else:
		redirect(reverse('index'))

def edit(request, id):
	if request.user.is_staff:
		forms = ArticleForm(request.POST)
		article = get_object_or_404(Article, pk=id)
		if forms.is_valid():
			article.title = forms.cleaned_data['title']
			article.contains = forms.cleaned_data['contains']
			article.save()
			return redirect(reverse('index'))
		else:
			forms = ArticleForm(initial={'title':article.title,'author':article.author,'contains':article.contains})
			return render(request, 'blog/add.html', {'forms':forms})
	else:
		redirect(reverse('index'))

def delete(request, id):
	if request.user.is_staff:
		article = get_object_or_404(Article, pk=id)
		article.delete()
		return redirect(reverse('index'))
	else:
		redirect(reverse('index'))

def comment(request, id):
	if request.user.is_authenticated:
		article = get_object_or_404(Article, pk=id)
		forms = CommentForm(request.POST)
		if forms.is_valid():
			_comment = Comment()
			_comment.article = article
			_comment.author = request.user
			_comment.contains = forms.cleaned_data['contains']
			_comment.save()
			return redirect(reverse('index'))
		else:
			return render(request, 'blog/add.html', {'forms':forms})
	else:
		redirect(reverse('index'))