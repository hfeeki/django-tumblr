from django.shortcuts import render_to_response
from tumblog.blog.models import Post
import datetime

def singlepage(request, inyear, inmonth, inday, string):
	post = Post.objects.get(date__year=inyear, date__month=inmonth, date__day=inday, urltitle=string)
	title = post.title
	whereami = "this is ridiculous"
	return render_to_response('single.html', locals())