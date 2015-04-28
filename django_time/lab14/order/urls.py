from django.conf.urls import patterns, include, url
from order import views
from order.views import OrderIndexView, OrderDetailView, CustomerDetailView, ProductDetailView, CustomerCreateView, OrderCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', OrderIndexView.as_view(), name='order_index'),
    url(r'^customer/list/$', views.list_customers, name='list_customers'),
    url(r'^product/list/$', views.list_products, name='list_products'),
    url(r'^detail/(?P<order_id>\d+)/$', login_required(OrderDetailView.as_view()), name='order'),
    url(r'^customer/detail/(?P<customer_slug>[\w\-]+)/$', login_required(CustomerDetailView.as_view()), name='customer'),
    url(r'^product/detail/(?P<product_id>\d+)/$', login_required(ProductDetailView.as_view()), name='product'),
    url(r'^customer/add/$', login_required(CustomerCreateView.as_view()), name='add_customer'),
    url(r'^customer/edit/(?P<customer_id>\d+)/$', views.edit_customer, name='edit_customer'),
    url(r'^product/add/$', views.add_product, name='add_product'),
    url(r'^product/edit/(?P<product_id>\d+)/(?P<stock_id>\d+)/$', views.edit_product, name='edit_product'),
    url(r'^add/$', login_required(OrderCreateView.as_view()), name='add_order'),
    #url(r'^edit/$', views.edit_order, name='edit_order'),
    url(r'^customer/ajax/list/$', views.ajax_list_products, name='ajax_list_products'),
    url(r'^customer/add/rest/$', views.add_customer_rest, name='add_customer_rest'),
)
