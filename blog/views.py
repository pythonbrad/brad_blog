from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
	articles = Article.objects.order_by('-pub_date').filter(is_visible=True)
	return render(request, 'blog/index.html', {'articles':articles})

def add(request):
	if request.user.is_authenticated:
		forms = ArticleForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect(reverse('index'))
		else:
			return render(request, 'blog/add.html', {'forms':forms})
	else:
		redirect(reverse('index'))

def edit(request, id):
	if request.user.is_authenticated:
		forms = ArticleForm(request.POST)
		article = get_object_or_404(Article, pk=id)
		if forms.is_valid():
			article.title = forms.cleaned_data['title']
			article.author = forms.cleaned_data['author']
			article.contains = forms.cleaned_data['contains']
			article.save()
			return redirect(reverse('index'))
		else:
			forms = ArticleForm(initial={'title':article.title,'author':article.author,'contains':article.contains})
			return render(request, 'blog/add.html', {'forms':forms, 'article':article})
	else:
		redirect(reverse('index'))

def delete(request, id):
	if request.user.is_authenticated:
		article = get_object_or_404(Article, pk=id)
		article.delete()
		return redirect(reverse('index'))
	else:
		redirect(reverse('index'))