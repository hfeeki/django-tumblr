from django.shortcuts import render_to_response
from django_tumblog_proj.apps.pages.models import Page
import datetime

def singlepage(request, string):
	post = Page.objects.get(slug=string)
	pages = Page.objects.order_by('title')
	return render_to_response('page_single.html', locals())# Create your views here.
