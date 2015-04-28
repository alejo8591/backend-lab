from django.shortcuts import render
from order.models import Order, Customer, Product, Stock

def index(request):

    context = {}

    orders = Order.objects.all()

    context.update({'orders':orders, 'title': 'Listado de Ordenes'})

    return render(request, 'index.html', context)


def order(request, order_id):

    context = {}
    try:
        order = Order.objects.get(id=order_id)

        context.update({'order':order, 'title': 'Detalle de la Orden'})

    except Order.DoesNotExist:

        context.update({'error': True})

    return render(request, 'detail.html', context)


def customer(request, customer_id):

    context = {}

    try:
        customer = Customer.objects.get(id=customer_id)

        context.update({'customer':customer, 'title': 'Detalle del Cliente'})

    except Customer.DoesNotExist:
        context.update({'error': True})

    return render(request, 'customer_detail.html', context)


def product(request, product_id):

    context = {}

    try:
        product = Product.objects.get(id=product_id)

        context.update({'product':product,'title': 'Detalle del Cliente'})
        try:
            stock = Stock.objects.get(stock_product_id=product_id)

            context.update({'stock':stock})

        except Stock.DoesNotExist:

            context.update({'error_stock':True})

    except Product.DoesNotExist:
        context.update({'error': True})

    return render(request, 'product_detail.html', context)
