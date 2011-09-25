from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

	url(r'^page/1$', 'django_tumblog_proj.apps.tumblog.entries.views.pageone', name='homepage'),
	url(r'^page/(\d+)$', 'django_tumblog_proj.apps.tumblog.entries.views.page', name='additionalpages'),
	
	url(r'^(\d{4})/(\d{1,2})/(\d{1,2})/(\S+)/$', 'django_tumblog_proj.apps.tumblog.blog.views.singlepage', name='single'),
	# url(r'^quote/(\d+)/$', 'django_tumblog_proj.apps.tumblog.quotes.views.singlequote', name="single_quote"),
	# url(r'^link/(\d{4})/(\d{1,2})/(\d{1,2})/(\S+)/$', 'django_tumblog_proj.apps.tumblog.links.views.singlepage', name='single_link'),

    #url(r'^archives/(\d{4})/(\d{1,2})/\d{1,2}/$', 'tumblog.entries.views.dayarchive', name='dayarchive'),
)