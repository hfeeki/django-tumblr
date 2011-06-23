from django.shortcuts import render_to_response
from django.shortcuts import redirect
from tumblog.entries.models import TumbleItem
import datetime


def homepage(request):
	tumble_item_list = TumbleItem.objects.all().order_by('-pub_date')[:10]
	not_used_list = TumbleItem.objects.all().order_by('-pub_date')[11:]
	empty = not not_used_list
	return render_to_response('homepage.html', locals())
	
def page(request, indig):
	page_number = int(indig)
	next_page= page_number+1
	previous_page=page_number-1
	startpost = (page_number*5)+1
	endpost = (page_number+1)*5
	tumble_item_list = TumbleItem.objects.all().order_by('-pub_date')[startpost:endpost]
	empty = not tumble_item_list
	not_used_list = TumbleItem.objects.all().order_by('-pub_date')[(endpost+1):]
	more = not not_used_list
	return render_to_response('page.html', locals())
	
def pageone(request):
	return redirect('/')