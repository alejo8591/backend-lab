#-*- encoding:utf-8 -*-
from django.db import models
import datetime, pytz

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

    date_created_customer = models.DateTimeField(auto_now=True)

    date_updated_customer = models.DateTimeField()


    def save(self, *args, **kwargs):
        # http://stackoverflow.com/questions/12015170/how-do-i-automatically-get-the-timezone-offset-for-my-local-time-zone
        now_utc = pytz.utc.localize(datetime.datetime.now())

        #self.date_updated_customer = datetime.datetime.now()
        self.date_updated_customer = now_utc.astimezone(pytz.timezone('America/Bogota'))

        super(Customer, self).save(*args, **kwargs)

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

    date_created_product = models.DateTimeField(auto_now=True)

    date_updated_product = models.DateTimeField()


    def save(self, *args, **kwargs):
        # http://stackoverflow.com/questions/12015170/how-do-i-automatically-get-the-timezone-offset-for-my-local-time-zone
        now_utc = pytz.utc.localize(datetime.datetime.now())

        #self.date_updated_product = datetime.datetime.now()
        self.date_updated_product = now_utc.astimezone(pytz.timezone('America/Bogota'))

        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} - {1}".format(str(self.id), str(self.product_name))


class Stock(models.Model):
    stock_product_id = models.ForeignKey('Product',
                                    verbose_name='producto',
                                    help_text='Stock del Producto.')

    stock_quantity = models.IntegerField(max_length=24,
                                    verbose_name='Cantidad',
                                    help_text='Cantidad del Producto.')

    date_created_stock = models.DateTimeField(auto_now=True)

    date_updated_stock = models.DateTimeField()


    def save(self, *args, **kwargs):
        # http://stackoverflow.com/questions/12015170/how-do-i-automatically-get-the-timezone-offset-for-my-local-time-zone
        now_utc = pytz.utc.localize(datetime.datetime.now())

        #self.date_updated_stock = datetime.datetime.now()
        self.date_updated_stock = now_utc.astimezone(pytz.timezone('America/Bogota'))

        super(Customer, self).save(*args, **kwargs)


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

    date_updated_order = models.DateTimeField()


    def save(self, *args, **kwargs):
        # http://stackoverflow.com/questions/12015170/how-do-i-automatically-get-the-timezone-offset-for-my-local-time-zone
        now_utc = pytz.utc.localize(datetime.datetime.now())

        #self.date_updated_order = datetime.datetime.now()
        self.date_updated_order = now_utc.astimezone(pytz.timezone('America/Bogota'))

        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.order_customer_id)
