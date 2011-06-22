from django.db import models
from django.conf import settings

class Tweet(models.Model):
	pub_time = models.DateTimeField()
	twitter_id = models.BigIntegerField()
	text = models.TextField()
	username = models.TextField()
	
	def __unicode__(self):
		return u'%s %s' % (self.text, self.pub_time)
