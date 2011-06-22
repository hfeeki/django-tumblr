from django.db import models
from django.contrib.auth.models import User 

class Page(models.Model):
	author=models.ForeignKey(User)
	title=models.CharField(max_length=100)
	post=models.TextField()
	slug=models.SlugField(max_length=100)
		
	def get_absolute_url(self):
		return self.slug
		
	def __unicode__(self):
		return self.title