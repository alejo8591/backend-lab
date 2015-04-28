from order.models import Customer, Product, Stock, Order
from autofixture import generators, register, AutoFixture

import random

types = ("Hardware", "Software", "Test-Software", "Test-Hardware", "Apps", "BigData",)
products = ("Casio 33W", "Lumia 34", "Cable USB", "Quanta 4G", "Magic Mouse", "Moto G",)

class CustomerFixture(AutoFixture):
    """
        customer_name = models.CharField(max_length=128,
                                        blank=True, null=True,
                                        verbose_name='Nombre',
                                        help_text='Ingrese el Nombre Completo.')

        customer_address = models.CharField(max_length=64,
                                        blank=True, null=True,
                                        verbose_name='Dirección',
                                        help_text='Ingrese la Direccion Completa.')

        customer_phone = models.CharField(max_length=24,
                                        blank=True, null=True,
                                        verbose_name='Teléfono',
                                        help_text='Ingrese el Teléfono.')
    """
    field_values = {
		'customer_name': generators.FirstNameGenerator(),
		'customer_address': generators.SmallIntegerGenerator(min_value=1240, max_value=9999),
        'customer_phone': generators.IntegerGenerator(min_value=124000, max_value=999999)
	}

class ProductFixture(AutoFixture):
    """
        product_name = models.CharField(max_length=128,
                                        verbose_name='Nombre del Producto',
                                        help_text='Indique Nombre del Producto.')

        product_price = models.DecimalField(max_digits=64,
                                        decimal_places = 2,
                                        verbose_name='Precio',
                                        help_text='Precio del Producto.')

        product_type = models.CharField(max_length=128,
                                        verbose_name='Tipo de Producto',
                                        help_text='Indique el Tipo de Producto.')

        product_description = models.TextField(max_length=128,
                                        verbose_name='Descripción de Producto',
                                        help_text='Indique el Tipo de Producto.')
    """
    field_values = {
		'product_name': generators.random.choice(products),
		'product_price': generators.PositiveIntegerGenerator(),
        'product_type': generators.random.choice(types),
        'product_description': generators.LoremGenerator()
	}

class StockFixture(AutoFixture):
    """
        stock_product_id = models.ForeignKey('Product',
                                        verbose_name='producto',
                                        help_text='Stock del Producto.')

        stock_quantity = models.IntegerField(max_length=24,
                                        verbose_name='Cantidad',
                                        help_text='Cantidad del Producto.')
    """

    field_values = {
		'stock_quantity': generators.SmallIntegerGenerator(min_value=1, max_value=9999),
	}

class OrderFixture(AutoFixture):
    """
        order_customer_id = models.ForeignKey('Customer',
                                        verbose_name='Cliente',
                                        help_text='Seleccione el Nombre del Cliente.')

        order_product_id = models.ForeignKey('Product',
                                        verbose_name='Producto',
                                        help_text='Seleccione el Producto(s).')

        order_amount = models.DecimalField(max_digits=64,
                                        decimal_places = 2,
                                        verbose_name='Cantidad',
                                        help_text='Cantidad del Producto.')
    """

    field_values = {
		'order_amount': generators.SmallIntegerGenerator(min_value=1, max_value=10),
	}

register(Customer, CustomerFixture)
register(Product, ProductFixture)
register(Stock, StockFixture)
register(Order, OrderFixture)
