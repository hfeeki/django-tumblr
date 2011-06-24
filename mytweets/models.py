from django.db import models
from django.conf import settings
import twitter
import datetime


class Tweet(models.Model):
	pub_time = models.DateTimeField()
	twitter_id = models.BigIntegerField()
	text = models.TextField()
	username = models.TextField()
	
	def __unicode__(self):
		return u'%s %s' % (self.text, self.pub_time)
		
	def getTweets(self):
		import twitter
		self.api = 
		
class TwitterSyncr():
	def __init__(self):
		self.api = twitter.Api()
		
	def getTweets(self):
		import datetime
		statuses = self.api.GetUserTimeline("willvanwazer") #This needs to be changed for other people?
		for s in statuses:
			if s.text[:1] == "@":
				#nothing to see here
			else:
				Tweet.objects.get_or_create(pub_time= datetime.now(), text=s.text, username="willvanwazer", twitter_id=s.id)

#TODO: Want to make import time actual tweet time. Need to parse twitter time object