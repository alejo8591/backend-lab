from django.shortcuts import render
from order.models import Order

def index(request):
    orders = Order.objects.all()

    context = {'orders':orders, 'title': 'Listado de Ordenes'}

    return render(request, 'index.html', context)

def order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)

        context = {'order':order, 'title': 'Detalle de la Orden'}

    except Order.DoesNotExist:
        context = {'error': True}

    return render(request, 'detail.html', context)
