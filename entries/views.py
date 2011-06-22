from django.shortcuts import render_to_response
from tumblog.entries.models import TumbleItem
import datetime


def homepage(request):
	context = {
		'tumble_item_list' : TumbleItem.objects.all().order_by('-pub_date')[:10]
	}
	return render_to_response('homepage.html', context)