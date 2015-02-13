from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response, RequestContext
from order.models import Order, Customer, Product, Stock
from order.forms import CustomerForm, ProductForm, StockForm, OrderForm
from django.contrib.auth.decorators import login_required
from datetime import datetime


def order_index(request):

    context = {}

    orders = Order.objects.all()

    context.update({'orders':orders, 'title': 'Listado de Ordenes'})

    #return render(request, 'order/index.html', context)
    return render_to_response('order_index.html', context, context_instance=RequestContext(request))


@login_required
def order(request, order_id):

    context = {}
    try:
        order = Order.objects.get(id=order_id)

        context.update({'order':order, 'title': 'Detalle de la Orden'})

    except Order.DoesNotExist:

        context.update({'error': True})

    return render(request, 'detail.html', context)


@login_required
def customer(request, customer_slug):

    """
        For update tuples
        >>> from order.models import Customer
        >>> customers = Customer.objects.all()
        >>> for customer in customers.iterator():
        ...     customer.save()
    """

    context = {}

    try:
        customer = Customer.objects.get(customer_slug=customer_slug)

        context.update({'customer':customer, 'title': 'Detalle del Cliente'})

    except Customer.DoesNotExist:
        context.update({'error': True})

    return render(request, 'customer_detail.html', context)


@login_required
def product(request, product_id):

    context = {}

    try:
        product = Product.objects.get(id=product_id)

        context.update({'product': product,'title': 'Detalle del Producto'})
        try:
            stock = Stock.objects.get(stock_product_id=product_id)

            context.update({'stock':stock})

        except Stock.DoesNotExist:

            context.update({'error_stock':True})

    except Product.DoesNotExist:
        context.update({'error': True})

    return render(request, 'product_detail.html', context)


@login_required
def add_customer(request):

    if request.method == 'POST':

        form = CustomerForm(request.POST)

        if form.is_valid():
            """
                Este método save () acepta un argumento cometer palabra clave opcional,
                que acepta Verdadero o Falso. Si se llama a save () con comprometes = False,
                entonces se volverá un objeto que aún no se ha guardado en la base de datos.
                En este caso, le toca a usted para llamar a save() en la instancia del modelo resultante.
                Esto es útil si usted quiere hacer un tratamiento
                personalizado en el objeto antes de guardarlo,
                o si desea utilizar una de las opciones especializadas de ahorro de modelo.
                cometer es true de forma predeterminada.
            """
            form.save()

            return redirect(order_index)

        else:
            print(form.errors)

    else:
        context = {'form': CustomerForm()}
    return render(request, 'add_customer.html',context)


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
def add_order(request):

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(order_index)
        else:
            print(form.errors)

    else:
        context = {'form':OrderForm()}

    return render(request, 'add_order.html',context)


@login_required
def list_customers(request):

    context = {}

    customers = Customer.objects.all()

    context.update({'customers':customers, 'title': 'Listado de Clientes'})

    return render(request, 'list_customers.html', context)


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
