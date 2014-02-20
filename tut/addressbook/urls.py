from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import contacts.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', contacts.views.ListContactView.as_view(), name='contact-list',),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^new/$', contacts.views.CreateContactView.as_view(), name='contact-new',),
)

# Static URL files
urlpatterns += staticfiles_urlpatterns()
