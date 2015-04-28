# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('customer_name', models.CharField(help_text='Ingrese el Nombre Completo.', max_length=128, blank=True, verbose_name='Name', null=True)),
                ('customer_address', models.CharField(help_text='Ingrese la Direccion Completa.', max_length=64, blank=True, verbose_name='Dirección', null=True)),
                ('customer_phone', models.CharField(help_text='Ingrese el Teléfono.', max_length=24, blank=True, verbose_name='Teléfono', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('order_amount', models.DecimalField(max_digits=64, help_text='Ingrese el Teléfono.', verbose_name='Teléfono', decimal_places=2)),
                ('order_date', models.DateField(auto_now=True)),
                ('order_customer_id', models.ForeignKey(help_text='Seleccione el Nombre del Cliente.', to='order.Customer', verbose_name='Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('product_price', models.DecimalField(max_digits=64, help_text='Precio del Producto.', verbose_name='Precio', decimal_places=2)),
                ('product_name', models.CharField(help_text='Indique Nombre del Producto.', max_length=128, verbose_name='Nombre del Producto')),
                ('product_type', models.CharField(help_text='Indique el Tipo de Producto.', max_length=128, verbose_name='Tipo de Producto')),
                ('product_description', models.TextField(help_text='Indique el Tipo de Producto.', max_length=128, verbose_name='Descripción de Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('stock_quantity', models.IntegerField(help_text='Cantidad del Producto.', max_length=24, verbose_name='Cantidad')),
                ('stock_product_id', models.ForeignKey(help_text='Stock del Producto.', to='order.Product', verbose_name='producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='order_product_id',
            field=models.ForeignKey(help_text='Seleccione el Producto(s).', to='order.Product', verbose_name='Prodcuto'),
            preserve_default=True,
        ),
    ]
