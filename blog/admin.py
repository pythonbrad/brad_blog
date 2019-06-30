from django.contrib import admin
from .models import Article
from .models import Comment


class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'pub_date', 'is_visible']


class CommentAdmin(admin.ModelAdmin):

    list_display = ['author', 'pub_date', 'is_visible']


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
