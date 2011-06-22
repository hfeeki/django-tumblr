from django.db import models

# Create your models here.
class Link(models.Model):
	link = models.URLField()
	title= models.CharField(mex_length=100)
	comment = models.TextField()
	date= models.DateTimeField()
	
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return self.link