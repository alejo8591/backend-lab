#-*- encoding:utf-8 -*-
from django.db import models

class Customer(models.Model):
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

    def __str__(self):
        return self.customer_name


class Product(models.Model):
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

    def __str__(self):
        return self.product_name


class Stock(models.Model):
    stock_product_id = models.ForeignKey('Product',
                                    verbose_name='producto',
                                    help_text='Stock del Producto.')

    stock_quantity = models.IntegerField(max_length=24,
                                    verbose_name='Cantidad',
                                    help_text='Cantidad del Producto.')


class Order(models.Model):
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

    order_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.order_customer_id)
