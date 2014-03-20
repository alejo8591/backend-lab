from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'bevolist.views.index', name='bevolist-index'),
	url(r'^(?P<item_id>\d+)/$', 'bevolist.views.details', name='bevolist-details'),
)