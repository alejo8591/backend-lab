from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response, RequestContext, HttpResponse
from order.models import Order, Customer, Product, Stock
from order.forms import CustomerForm, ProductForm, StockForm, OrderForm
from datetime import datetime
import json

from order.serializer import CustomerSerializer, ProductSerializer, StockSerializer, OrderSerializer
from rest_framework import viewsets

from django.views.generic import TemplateView, FormView, RedirectView, DetailView, CreateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class OrderIndexView(TemplateView):

    template_name = 'order_index.html'

    def get_context_data(self, **kwargs):

        context = super(OrderIndexView, self).get_context_data(**kwargs)

        context.update({'orders':Order.objects.all(), 'title': 'Listado de Ordenes'})

        return context

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


class OrderDetailView(DetailView):

    model = Order
    pk_url_kwarg = 'order_id'
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)

        context.update({'title': 'Listado de Ordenes'})

        return context


class CustomerDetailView(DetailView):

    model = Customer
    slug_url_kwarg = 'customer_slug'
    slug_field = 'customer_slug'
    template_name = 'customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)

        context.update({'title': 'Detalle del Cliente'})

        return context


class ProductDetailView(DetailView):

    model = Product
    pk_url_kwarg = 'product_id'
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        """
            They are passed in the old way.

            You access them via self.args and self.kwargs,
            for positional and keyword arguments respectively.
            In your case, self.kwargs['id'] would do the trick.

            Edit because you've overridden get() but not preserved the signature.
            If you're overriding a method, always do def get(self, request, *args, **kwargs)
        """

        stock = Stock.objects.get(stock_product_id=int(self.kwargs['product_id']))

        context.update({'title': 'Listado de Ordenes', 'stock': stock})

        return context


class CustomerCreateView(CreateView):

    model = Customer
    template_name = 'add_customer.html'
    fields = ['customer_name', 'customer_phone', 'customer_address']
    form_class = CustomerForm
    success_url = '/order/'


class OrderCreateView(CreateView):

    model = Order
    template_name = 'add_order.html'
    fields = ['order_customer_id', 'order_product_id', 'order_amount']
    form_class = OrderForm
    success_url = '/order/'


@login_required
def add_product(request):

    if request.method == 'POST':

        product_form = ProductForm(request.POST, prefix='product')
        stock_form = StockForm(request.POST, prefix='stock')

        if product_form.is_valid() and stock_form.is_valid():

            product_save = product_form.save()

            stock_save = stock_form.save(commit=False)

            stock_save.stock_product_id = product_save

            stock_save.save()

            return redirect(order_index)

        else:
            print(form.errors)

    else:
        context = {'product_form': ProductForm(prefix='product'), 'stock_form': StockForm(prefix='stock')}

    return render(request, 'add_product.html',context)


@login_required
def list_customers(request):

    context = {}

    customers = Customer.objects.all()

    context.update({'customers':customers, 'title': 'Listado de Clientes'})

    visits = request.session.get('visits')

    if not visits:
        visits = 1

    reset_last_time = False

    last_visit = request.session.get('last_visit')

    response = render(request, 'list_customers.html', context)

    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], '%Y-%m-%d %H:%M:%S')

        if (datetime.now() - last_visit_time).seconds > 0:
            visits += 1
            reset_last_visit_time = True

    else:
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits

        response.set_cookie('last_visit', request.session['last_visit'])
        response.set_cookie('visits', request.session['visits'])

    context.update({'visits': visits})

    return response


@login_required
def list_products(request):

    context = {}

    products = Product.objects.all()

    visits = int(request.COOKIES.get('visits', '1'))

    if not visits:
        visits = 1

    context.update({'products':products, 'title': 'Listado de Productos', 'visits': visits})

    reset_last_visit_time = False

    response = render(request, 'list_products.html', context)

    if 'last_visit' in request.COOKIES:

        last_visit = request.COOKIES['last_visit']

        last_visit_time = datetime.strptime(last_visit[:-7], '%Y-%m-%d %H:%M:%S')

        if (datetime.now() - last_visit_time).seconds > 0:
            visits += 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True

        context['visits'] = visits

        response = render(request, 'list_products.html', context)

    if reset_last_visit_time:

        response.set_cookie('last_visit', datetime.now())
        response.set_cookie('visits', visits)

    return response


@login_required
def edit_customer(request, customer_id):

    context = {}

    try:
        customer = get_object_or_404(Customer, id=customer_id)

        if request.method == 'POST':

            form = CustomerForm(request.POST)

            if form.is_valid():
                customer.customer_name = form.cleaned_data['customer_name']
                customer.customer_address = form.cleaned_data['customer_address']
                customer.customer_phone = form.cleaned_data['customer_phone']

                customer.save()

                return HttpResponseRedirect('/order/customer/detail/%s/' % customer.id)

        else:
            customer_data = {
                'customer_name': customer.customer_name,
                'customer_address': customer.customer_address,
                'customer_phone': customer.customer_phone
            }

            form = CustomerForm(initial=customer_data)

    except Customer.DoesNotExist:

        context.update({'error': True})

    context.update({'title': 'Editar Cliente', 'form': form, 'update': True, 'customer': customer})

    return render(request, 'add_customer.html', context)


@login_required
def edit_product(request, product_id, stock_id):

    context = {}

    try:
        product = get_object_or_404(Product, id=product_id)
        stock = get_object_or_404(Stock, id=stock_id)

        if request.method == 'POST':

            product_form = ProductForm(request.POST, prefix='product')
            stock_form = StockForm(request.POST, prefix='stock')

            if product_form.is_valid() and stock_form.is_valid():
                product.product_name = product_form.cleaned_data['product_name']
                product.product_type = product_form.cleaned_data['product_type']
                product.product_price = product_form.cleaned_data['product_price']
                product.product_description = product_form.cleaned_data['product_description']

                stock.stock_quantity = stock_form.cleaned_data['stock_quantity']

                product.save()
                stock.save()

                """
                    product_update = product_form.save()

                    stock_update = stock_form.save(commit=False)

                    stock_update.stock_product_id = product_update

                    stock_update.save()
                """

                return HttpResponseRedirect('/order/product/detail/%s/' % product.id)

        else:
            stock_data = {
                'stock_quantity': stock.stock_quantity
            }

            product_data = {
                'product_name': product.product_name,
                'product_type': product.product_type,
                'product_price': product.product_price,
                'product_description': product.product_description
            }

            product_form = ProductForm(initial=product_data, prefix='product')
            stock_form = StockForm(initial=stock_data, prefix='stock')

    except Customer.DoesNotExist:

        context.update({'error': True})

    context.update({
        'title': 'Editar Cliente',
        'product_form': product_form,
        'stock_form': stock_form,
        'update': True,
        'product': product,
        'stock': stock})

    return render(request, 'add_product.html', context)


""" AJAX """
@login_required
def like_product(request):

    product_id = None
    likes = 0
    if request.is_ajax():
        product_id = request.POST['product_id']

        if product_id:
            product = Product.objects.get(id=product_id)

            if product:
                product.product_likes = 0 if product.product_likes == None else int(product.product_likes)
                likes = product.product_likes + 1
                product.product_likes = likes
                product.save()

    return HttpResponse(likes)


@login_required
def ajax_list_products(request):

    if request.is_ajax():

        customers = Customer.objects.values('customer_name', 'customer_phone', 'customer_address', 'id', 'customer_slug')

        results = [customer for customer in customers]

        return HttpResponse(json.dumps(results), content_type='application/json')

@login_required
def add_customer_rest(request):
    return render(request, 'add_product_ajax.html', {})

""" REST """
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
