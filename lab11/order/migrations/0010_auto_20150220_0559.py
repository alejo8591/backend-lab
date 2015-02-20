# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20150220_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_likes',
            field=models.IntegerField(blank=True, default=0, null=True),
            preserve_default=True,
        ),
    ]
