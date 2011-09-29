from django.db import models
from django.contrib.auth.models import User 
import re
import datetime

class Post(models.Model):
	author=models.ForeignKey(User)
	date=models.DateTimeField(default=datetime.datetime.now)
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
	date= models.DateTimeField(default=datetime.datetime.now)
	slug =models.SlugField(max_length=100)
	
	def __unicode__(self):
		return self.title[:15]
		
	def get_absolute_url(self):
		return self.link

class Quote(models.Model):
#	author=models.ForeignKey(User)
	date=models.DateTimeField(default=datetime.datetime.now)
	quote=models.TextField()
	source=models.TextField()
	
	def __unicode__(self):
		return self.quote[:15]
	
	def get_absolute_url(self):
		return "/blog/quote/%s" % (self.id)
		
class Photo(models.Model):
    """A container for photos to be posted on the blag."""
    date = models.DateTimeField(default=datetime.datetime.now)
    source = models.URLField(blank=False, verify_exists=False)
    comment = models.TextField(blank=True, null=True)
    
    def get_absolute_url(self):
        return self.source
        
    def __unicode__(self):
        return "Photo %s: %s..." % (self.id, self.comment[:10])
        
class Video(models.Model):
    """A container for videos to be posted on the blag."""
    date = models.DateTimeField(default=datetime.datetime.now)
    embed_code = models.TextField()
    comment = models.TextField(blank=True)

    def get_absolute_url(self):
        return "video/%s" % (self.id)

    def __unicode__(self):
        return "Video %s: %s..." % (self.id, self.comment[:10])

