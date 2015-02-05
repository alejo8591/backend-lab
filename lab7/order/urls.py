from django.conf.urls import patterns, include, url
from order import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<order_id>\d+)/$', views.order, name='order'),
    url(r'^customer/detail/(?P<customer_id>\d+)/$', views.customer, name='customer'),
    url(r'^product/detail/(?P<product_id>\d+)/$', views.product, name='product'),
    url(r'^customer/add/$', views.add_customer, name='add_customer'),
    url(r'^product/add/$', views.add_product, name='add_product'),
    url(r'^add/$', views.add_order, name='add_order'),
)
