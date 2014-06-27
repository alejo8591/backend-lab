from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cidei.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/$', 'list.views.index', name='list-index'),
    url(r'^list/(?P<item_id>\d+)/$', 'list.views.details', name='list-details'),
)
