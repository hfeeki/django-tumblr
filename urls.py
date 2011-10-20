from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django_tumblog_proj.apps.tumblog.entries.views.homepage', name='homepage'),
    url(r'^blog/', include('django_tumblog_proj.apps.tumblog.urls')),
    url(r'^page/(\S+)/$', 'django_tumblog_proj.apps.pages.views.singlepage'),
	url(r'^mdst-midterm/$', direct_to_template, {'template': 'mdst_midterm.html'}),
)
# 
# urlpatterns += staticfiles_urlpatterns()