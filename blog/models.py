from django.db import models
from django.contrib.auth.models import User 
import re

class Post(models.Model):
	author=models.ForeignKey(User)
	date=models.DateTimeField()
	title=models.CharField(max_length=100)
	post=models.TextField()
	urltitle=models.SlugField(max_length=100)
	
	def save(self):
		self.urltitle = re.sub("\W+" , "-", self.title.lower())
		super(Post, self).save()
		
	def get_absolute_url(self):
		import datetime
		return "/%i/%i/%i/%s" % (self.date.year, self.date.month, self.date.day, self.urltitle) 
	
	def __unicode__(self):
		return self.title