from django.shortcuts import render_to_response
from tumblog.quotes.models import Quote
import datetime

def singlequote(request, inid):
	quote = Quote.objects.get(pk=inid)
	return render_to_response('quotesingle.html', locals())
	
#Still shows template does not exist error, but at least we are somewhere.