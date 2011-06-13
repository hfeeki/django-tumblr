from django.shortcuts import render_to_response
from tumblog.blog.models import Post
import datetime

def homepage(request):
	current_date = datetime.datetime.now()
	posts = Post.objects.order_by('date')
	return render_to_response('homepage.html', locals())

def singlepage(request, year, month, day, string):
	post = Post.objects.get(year__exact=year, urltitle__exact=string)
	