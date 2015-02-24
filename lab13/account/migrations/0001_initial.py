# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('userprofile_website', models.URLField(blank=True)),
                ('userprofile_picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('userprofile_identfication', models.CharField(help_text='Numero de Identficacion', unique=True, verbose_name='Identificacion', max_length=24)),
                ('userprofile', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
