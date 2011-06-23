from django.db import models
from django.contrib.auth.models import User 

import datetime

class Quote(models.Model):
#	author=models.ForeignKey(User)
	date=models.DateTimeField()
	quote=models.TextField()
	source=models.TextField()
	
	def __unicode__(self):
		return self.quote
	
	def get_absolute_url(self):
		return "/quote/%s" % (self.id)