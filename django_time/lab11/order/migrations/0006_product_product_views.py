# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20150210_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_views',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
