# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 20:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_search_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 26, 20, 15, 14, 231331, tzinfo=utc), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='search',
            name='region_choices',
            field=models.CharField(choices=[('NA', 'North America'), ('EU', 'Europe'), ('AS', 'Asian'), ('OC', 'Oceania'), ('SA', 'South America'), ('SEA', 'South East Asia'), ('KR/JP', 'Korea/Japan')], max_length=5, verbose_name='region preference'),
        ),
        migrations.AlterField(
            model_name='search',
            name='team_choices',
            field=models.CharField(choices=[('DUOS', 'DUOS'), ('SQUADS', 'SQUADS'), ('DUOS FPS', 'DUOS FPS'), ('SQUADS FPS', 'SQUADS FPS')], max_length=10, verbose_name='team preference'),
        ),
    ]