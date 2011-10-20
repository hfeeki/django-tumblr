from django.shortcuts import render_to_response
from django_tumblog_proj.apps.tumblog.blog.models import Post
from django_tumblog_proj.apps.pages.models import Page

import datetime

def singlepage(request, inyear, inmonth, inday, string):
	post = Post.objects.get(date__year=inyear, date__month=inmonth, date__day=inday, urltitle=string)
	title = post.title
	pages = Page.objects.order_by('title')
	return render_to_response('single.html', locals())
