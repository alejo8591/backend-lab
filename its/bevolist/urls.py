from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'bevolist.views.index', name='bevolist-index'),
	url(r'^(?P<item_id>\d+)/$', 'bevolist.views.details', name='bevolist-details'),
	url(r'^category/$', 'bevolist.views.category', name='bevolist-category'),
	url(r'^category/(?P<slug>[\w]+)/$', 'bevolist.views.category_details', name='bevolist-category-details'),
)