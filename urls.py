from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tumblog.entries.views.homepage', name='homepage'),
	url(r'^(\d{4})/(\d{1,2})/(\d{1,2})/(\S+)/$', 'tumblog.blog.views.singlepage', name='single'),
	url(r'^quote/(\d+)/$', 'tumblog.quotes.views.singlequote', name="single_quote"),
	url(r'^link/(\d{4})/(\d{1,2})/(\d{1,2})/(\S+)/$', 'tumblog.links.views.singlepage', name='single_link'),
	#url(r'^(\d{4})/(\d{1,2})/\d{1,2}/$', 'tumblog.blog.views.dayarchive', name='dayarchive'),
    # url(r'^tumblog/', include('tumblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)