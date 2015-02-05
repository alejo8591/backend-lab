from django.shortcuts import render, redirect
from order.models import Order, Customer, Product, Stock
from order.forms import CustomerForm, ProductForm, StockForm, OrderForm

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

            return redirect(index)

        else:
            print(form.errors)

    else:
        context = {'form': CustomerForm()}
    return render(request, 'add_customer.html',context)

def add_product(request):

    if request.method == 'POST':

        product_form = ProductForm(request.POST, prefix='product')
        stock_form = StockForm(request.POST, prefix='stock')

        if product_form.is_valid() and stock_form.is_valid():

            product_save = product_form.save()

            stock_save = stock_form.save(commit=False)

            stock_save.stock_product_id = product_save

            stock_save.save()

            return redirect('index')

        else:
            print(form.errors)

    else:
        context = {'product_form': ProductForm(prefix='product'), 'stock_form': StockForm(prefix='stock')}

    return render(request, 'add_product.html',context)


def add_order(request):

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(index)
        else:
            print(form.errors)

    else:
        context = {'form':OrderForm()}
        
    return render(request, 'add_order.html',context)
