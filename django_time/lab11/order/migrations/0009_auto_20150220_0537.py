# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_product_product_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_like',
            new_name='product_likes',
        ),
    ]
