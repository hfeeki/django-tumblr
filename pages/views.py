from django.shortcuts import render_to_response
from tumblog.page.models import Page
import datetime

def singlepage(request, string):
	post = Post.objects.get(slug=string)
	return render_to_response('single.html', locals())# Create your views here.
