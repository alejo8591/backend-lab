# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_product_product_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_like',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
