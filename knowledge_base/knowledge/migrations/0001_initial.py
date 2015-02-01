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
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('alert', models.BooleanField(help_text='Check this if you want to be alerted when a new response is added.', default='KNOWLEDGE_ALERTS', verbose_name='Alert')),
                ('name', models.CharField(help_text='Enter your first and last name.', verbose_name='Name', max_length=64, blank=True, null=True)),
                ('email', models.EmailField(help_text='Enter a valid email address.', verbose_name='Email', max_length=75, blank=True, null=True)),
                ('title', models.CharField(help_text='Enter your question or suggestion.', max_length=255, verbose_name='Question')),
                ('body', models.TextField(help_text='Please offer details. Markdown enabled.', verbose_name='Description', blank=True, null=True)),
                ('status', models.CharField(db_index=True, choices=[('public', 'Public'), ('private', 'Private'), ('internal', 'Internal')], max_length=32, default='private', verbose_name='Status')),
                ('locked', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(to='knowledge.Category', blank=True)),
                ('user', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-added'],
                'verbose_name_plural': 'Questions',
                'verbose_name': 'Question',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('alert', models.BooleanField(help_text='Check this if you want to be alerted when a new response is added.', default='KNOWLEDGE_ALERTS', verbose_name='Alert')),
                ('name', models.CharField(help_text='Enter your first and last name.', verbose_name='Name', max_length=64, blank=True, null=True)),
                ('email', models.EmailField(help_text='Enter a valid email address.', verbose_name='Email', max_length=75, blank=True, null=True)),
                ('body', models.TextField(help_text='Please enter your response. Markdown enabled.', verbose_name='Response', blank=True, null=True)),
                ('status', models.CharField(db_index=True, choices=[('public', 'Public'), ('private', 'Private'), ('internal', 'Internal'), ('inherit', 'Inherit')], max_length=32, default='inherit', verbose_name='Status')),
                ('accepted', models.BooleanField(default=False)),
                ('question', models.ForeignKey(to='knowledge.Question', related_name='responses')),
                ('user', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['added'],
                'verbose_name_plural': 'Responses',
                'verbose_name': 'Response',
            },
            bases=(models.Model,),
        ),
    ]
