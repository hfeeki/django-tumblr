from django.db import models
from django.contrib.auth.models import User 
import re

class Post(models.Model):
	author=models.ForeignKey(User)
	date=models.DateTimeField()
	title=models.CharField(max_length=100)
	post=models.TextField()
	urltitle=models.SlugField(max_length=100)
		
	def get_absolute_url(self):
		import datetime
		return "/blog/%i/%i/%i/%s" % (self.date.year, self.date.month, self.date.day, self.urltitle) 
	
	def __unicode__(self):
		return self.title

class Link(models.Model):
	link = models.URLField(verify_exists=False)
	title= models.CharField(max_length=100)
	comment = models.TextField()
	date= models.DateTimeField()
	slug =models.SlugField(max_length=100)
	
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return self.link

class Quote(models.Model):
#	author=models.ForeignKey(User)
	date=models.DateTimeField()
	quote=models.TextField()
	source=models.TextField()
	
	def __unicode__(self):
		return self.quote
	
	def get_absolute_url(self):
		return "/blog/quote/%s" % (self.id)