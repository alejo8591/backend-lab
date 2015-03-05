from django.conf.urls import patterns, include, url
from order import views
from order.views import OrderIndexView, OrderDetailView

urlpatterns = patterns('',
    url(r'^$', OrderIndexView.as_view(), name='order_index'),
    url(r'^customer/list/$', views.list_customers, name='list_customers'),
    url(r'^product/list/$', views.list_products, name='list_products'),
    url(r'^detail/(?P<order_id>\d+)/$', OrderDetailView.as_view(), name='order'),
    url(r'^customer/detail/(?P<customer_slug>[\w\-]+)/$', views.customer, name='customer'),
    url(r'^product/detail/(?P<product_id>\d+)/$', views.product, name='product'),
    url(r'^customer/add/$', views.add_customer, name='add_customer'),
    url(r'^customer/edit/(?P<customer_id>\d+)/$', views.edit_customer, name='edit_customer'),
    url(r'^product/add/$', views.add_product, name='add_product'),
    url(r'^product/edit/(?P<product_id>\d+)/(?P<stock_id>\d+)/$', views.edit_product, name='edit_product'),
    url(r'^add/$', views.add_order, name='add_order'),
    #url(r'^edit/$', views.edit_order, name='edit_order'),
    url(r'^customer/ajax/list/$', views.ajax_list_products, name='ajax_list_products'),
    url(r'^customer/add/rest/$', views.add_customer_rest, name='add_customer_rest'),
)
