# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 15:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 25, 15, 1, 14, 313893, tzinfo=utc), verbose_name='date joined'),
        ),
    ]