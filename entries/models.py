from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from blog.models import Post
from mytweets.models import Tweet
from django.db.models.signals import post_save
from django.dispatch import receiver


class TumbleItem(models.Model):
	content_type = models.ForeignKey(ContentType)
	object_id= models.PositiveIntegerField()
	pub_date=models.DateTimeField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	
	class Meta:
		ordering = ('pub_date',)
	def __unicode__(self):
		return self.content_type.name

@receiver(post_save)
def my_callback(sender, **kwargs):
	if 'created' in kwargs:
		create=True
		ctype=ContentType.objects.get_for_model(instance)
		if ctype.name == 'Tweet':
			pub_date = instance.pub_time
		else:
			pub_date = instance.date
		if create:
			t = TumbleItem.objects.get_or_create(content_type=ctype, object_id=instance.id, pub_date=pub_date)