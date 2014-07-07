from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from app.views import CategoryViewSet, ItemViewSet

#from accounts.views import UserViewSet, UserProfileViewSet

from rest_framework.urlpatterns import format_suffix_patterns
"""
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'users', UserViewSet)
router.register(r'profile', UserProfileViewSet)
"""


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cidei.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/users/$', 'accounts.views.users_list'),
    #url(r'^api/v1/', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
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
    url(r'^login/$', 'accounts.views.user_login', name='user-login'), # ADD NEW PATTERN!
)

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

format_suffix_patterns(urlpatterns)