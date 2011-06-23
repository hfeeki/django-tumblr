from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class Link(models.Model):
#	author=models.ForeignKey(User)
	link = models.URLField(verify_exists=False)
	title= models.CharField(max_length=100)
	comment = models.TextField()
	date= models.DateTimeField()
	slug =models.SlugField(max_length=100)
	
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return self.link