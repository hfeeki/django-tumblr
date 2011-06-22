from django.db import models

# Create your models here.
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