from django.shortcuts import render_to_response
from tumblog.links.models import Link
import datetime

def singlepage(request, inyear, inmonth, inday, string):
	link = Link.objects.get(date__year=inyear, date__month=inmonth, date__day=inday, slug=string)
	return render_to_response('singledatetime.html', locals())

##Need to create a template here.