from django.conf.urls import patterns, include, url
from account.views import LoginView, user_logout

urlpatterns = patterns('',
    #url(r'^register/$', views.register, name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', user_logout, name='logout'),
)
