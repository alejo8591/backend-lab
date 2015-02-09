#http://stackoverflow.com/questions/714063/python-importing-modules-from-parent-folder
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import lab2

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab2.settings')

from order.models import Customer, Product, Stock, Order

import django
django.setup()

def populate():

    customer_one = add_customer(
        customer_name='Alejandro Romero',
        customer_address='Crr 20 # 23 - 24',
        customer_phone='337337'
    )

    product_one = add_product(
        product_name='Citizen #1',
        product_price=690700.23,
        product_type='Reloj',
        product_description='Reloj Citizen'
    )

    stock = {

    }

    stock_one = add_stock(
        stock_product_id=product_one,
        stock_quantity=10
    )

    order_one = add_order(
        order_customer_id=customer_one,
        order_product_id=product_one,
        order_amount=4
    )

    customer_two = add_customer(
        customer_name='Ferreira',
        customer_address='Crr 20 # 23 - 24',
        customer_phone='337337'
    )

    product_two = add_product(
        product_name='Fazer 22',
        product_price=990700.45,
        product_type='Reloj',
        product_description='Reloj Fazer'
    )

    stock_two = add_stock(
        stock_product_id=product_one,
        stock_quantity=4
    )

    order_two = add_order(
        order_customer_id=customer_two,
        order_product_id=product_two,
        order_amount=2
    )

    # Print out what we have added to the user.
    for product in Product.objects.all():
        for stock in Stock.objects.filter(stock_product_id=product):
            print("El producto {0} tiene un stock de {1}".format(str(product), str(stock.stock_quantity)))

    # Print out what we have customer orders.
    for customer in Customer.objects.all():
        for order in Order.objects.filter(order_customer_id=customer):
            print("El cliente {0} tiene una orden con #{1}".format(str(customer), str(order.id)))

# http://stackoverflow.com/questions/3394835/args-and-kwargs
def add_customer(**kwargs):
    customer = Customer.objects.get_or_create(customer_name=kwargs['customer_name'], customer_address=kwargs['customer_address'], customer_phone=kwargs['customer_phone'])[0]
    return customer

def add_product(**kwargs):
    product = Product.objects.get_or_create(product_name=kwargs['product_name'], product_price=kwargs['product_price'], product_type=kwargs['product_type'], product_description=kwargs['product_description'])[0]
    return product


def add_stock(**kwargs):
    stock = Stock.objects.get_or_create(stock_product_id=kwargs['stock_product_id'], stock_quantity=kwargs['stock_quantity'])[0]
    return stock

def add_order(**kwargs):
    order = Order.objects.get_or_create(order_customer_id=kwargs['order_customer_id'], order_product_id=kwargs['order_product_id'], order_amount=kwargs['order_amount'])[0]
    return order

# Start execution here!
if __name__ == '__main__':
    print( "Creando info en la BD...")
    populate()
