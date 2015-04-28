# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20150205_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_updated_customer',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 2, 5, 19, 56, 43, 152818, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
