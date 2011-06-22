from django.shortcuts import render_to_response
from tumblog.entries.models import TumbleItem
from tumblog.blog.models import Post
import datetime


def homepage(request):
	items = TumbleItem.objects.all()[:5]
	return render_to_response('homepage.html', locals())