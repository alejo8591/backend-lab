# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_customer_date_updated_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_updated_order',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 5, 21, 3, 16, 541356, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='date_updated_product',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 5, 21, 3, 20, 501167, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='date_updated_stock',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 5, 21, 3, 23, 111086, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_updated_customer',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
