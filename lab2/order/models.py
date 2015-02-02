from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=128,
                                    blank=True, null=True,
                                    verbose_name='Name',
                                    help_text='Ingrese el Nombre Completo.')

    customer_address = models.CharFiled(max_length=64,
                                    blank=True, null=True,
                                    verbose_name='Dirección',
                                    help_text='Ingrese la Direccion Completa.')

    customer_phone = models.CharFiled(max_length=24,
                                    blank=True, null=True,
                                    verbose_name='Teléfono',
                                    help_text='Ingrese el Teléfono.')

    def __str__(self):
        return self.customer_name
