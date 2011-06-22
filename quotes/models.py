from django.db import models
import datetime

class Quote(models.Model):
	date=models.DateTimeField()
	quote=models.TextField()
	source=models.TextField()
	
	def __unicode__(self):
		return self.quote