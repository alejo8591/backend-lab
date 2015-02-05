# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_created_customer',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 2, 5, 19, 43, 44, 168165, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='date_created_product',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 2, 5, 19, 43, 49, 39195, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='date_created_stock',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 2, 5, 19, 43, 52, 290398, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(help_text='Ingrese el Nombre Completo.', verbose_name='Nombre', blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_amount',
            field=models.DecimalField(max_digits=64, decimal_places=2, help_text='Cantidad del Producto.', verbose_name='Cantidad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_product_id',
            field=models.ForeignKey(to='order.Product', verbose_name='Producto', help_text='Seleccione el Producto(s).'),
            preserve_default=True,
        ),
    ]
