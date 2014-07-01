from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cidei.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.index', name="index"),
    url(r'^categories/$', 'app.views.categories', name="categories"),
    url(r'^categories/add/$', 'app.views.add_category', name="add-category"),
    url(r'^categories/(?P<slug>[\w-]+)/$', 'app.views.category', name="category"),
    url(r'^categories/(?P<slug>[\w-]+)/edit/$', 'app.views.edit_category', name="edit-category"),
    url(r'^categories/(?P<slug>[\w-]+)/delete/$', 'app.views.delete_category', name="delete-category"),
    url(r'^items/$', 'app.views.items', name="items"),
    url(r'^items/add/$', 'app.views.add_item', name="add-item"),
    url(r'^items/(?P<item_id>\d+)/$', 'app.views.item', name="item"),
    url(r'^items/(?P<item_id>\d+)/edit/$', 'app.views.edit_item', name='edit-item'),
    url(r'^items/(?P<item_id>\d+)/delete/$', 'app.views.delete_item', name='delete-item'),
    url(r'^items/ajax/$', 'app.views.ajax_items', name='ajax-items'),
    url(r'^items/ajax/(?P<item_id>\d+)/$', 'app.views.ajax_item', name='ajax-item'),
    url(r'^register/$', 'accounts.views.register', name='register'), # ADD NEW PATTERN!
)