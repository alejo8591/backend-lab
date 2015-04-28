# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_product_product_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_views',
        ),
    ]
