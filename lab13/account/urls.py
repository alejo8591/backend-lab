from django.conf.urls import patterns, include, url
from account.views import LoginView, RegisterView, LogoutView

urlpatterns = patterns('',
    #url(r'^register/$', views.register, name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
)
