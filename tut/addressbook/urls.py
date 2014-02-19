from django.conf.urls import patterns, include, url
import contacts.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', contacts.views.ListContactView.as_view(), name='contact-list',),
    url(r'^admin/', include(admin.site.urls)),
)
