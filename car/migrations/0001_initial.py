# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('engine', models.CharField(max_length=200, null=True, blank=True)),
                ('power', models.CharField(max_length=200, null=True, blank=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('color', models.CharField(max_length=200, null=True, blank=True)),
                ('price', models.CharField(max_length=200, null=True, blank=True)),
                ('detail', models.CharField(max_length=400, null=True, blank=True)),
                ('contact', models.CharField(max_length=200, null=True, blank=True)),
                ('gears', models.CharField(max_length=200, null=True, blank=True)),
                ('year', models.CharField(max_length=200, null=True, blank=True)),
                ('milage', models.CharField(max_length=200, null=True, blank=True)),
                ('posted_on', models.DateField(null=True, blank=True)),
            ],
        ),
    ]
