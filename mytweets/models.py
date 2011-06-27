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
		
class TwitterSyncr():
	def __init__(self):
		self.api = twitter.Api()
	
	@staticmethod	
	def getTweets(self):
		from tumblog.mytweets.models import Tweet
		import datetime
		statuses = self.api.GetUserTimeline("LIZard23") #This needs to be changed for other people?
		for s in statuses:
			if not s.text[:1] == "@":
				#Fixing the time, bitch
				t = datetime.datetime.strptime(s.created-at, "%a %b %d %H:%M:%S +0000 %Y")
				d = datetime.timedelta(hours=4)
				adjtime = t - d
				print adjtime
				Tweet.objects.get_or_create(pub_time= adjtime, text=s.text, username="willvanwazer", twitter_id=s.id)
#TODO: Want to make import time actual tweet time. Need to parse twitter time object