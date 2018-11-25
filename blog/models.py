from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=30)
	author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	contains = models.TextField(default='')
	pub_date = models.DateTimeField(default=timezone.now)
	is_visible = models.BooleanField(default=True)

	def __str__(self):
		return self.title