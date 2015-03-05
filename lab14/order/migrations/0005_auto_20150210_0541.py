# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20150205_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_slug',
            field=models.SlugField(blank=True, null=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created_customer',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_updated_customer',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created_product',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='date_created_stock',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
