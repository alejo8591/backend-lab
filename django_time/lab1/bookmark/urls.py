from django.conf.urls import patterns, include, url
from bookmark import views

import autofixture

autofixture.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^uploads/', views.uploads, name='uploads'),
)
