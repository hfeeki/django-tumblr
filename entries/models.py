from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from blog.models import Post
from mytweets.models import Tweet
from quotes.models import Quote
from links.models import Link
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string


class TumbleItem(models.Model):
	content_type = models.ForeignKey(ContentType)
	object_id= models.PositiveIntegerField()
	pub_date=models.DateTimeField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	
	class Meta:
		ordering = ('pub_date',)
	def __unicode__(self):
		return self.content_type.name
	def get_rendered_html(self):
		template_name = 'homepage_item_%s.html' % (self.content_type.name)
		return render_to_string(template_name, { 'object': self.content_object})

@receiver(post_save, sender=Post)
def my_callback(sender, instance, created, **kwargs):
	if created:
		c = ContentType.objects.get_for_model(instance)
		t = TumbleItem.objects.get_or_create(content_type=c, object_id=instance.id, pub_date=instance.date)

@receiver(post_save, sender=Link)
def link_callback(sender, instance, created, **kwargs):
	if created:
		c = ContentType.objects.get_for_model(instance)
		t = TumbleItem.objects.get_or_create(content_type=c, object_id=instance.id, pub_date=instance.date)

@receiver(post_save, sender=Quote)
def quote_callback(sender, instance, created, **kwargs):
	if created:
		c = ContentType.objects.get_for_model(instance)
		t = TumbleItem.objects.get_or_create(content_type=c, object_id=instance.id, pub_date=instance.date)

@receiver(post_save, sender=Tweet)
def tweet_callback(sender, instance, created, **kwargs):
	if created:
		c = ContentType.objects.get_for_model(instance)
		t = TumbleItem.objects.get_or_create(content_type=c, object_id=instance.id, pub_date=instance.pub_time)
		
##TO-DO here: implement callbacks for tweets, and other posts as necesary
# Rename my callback