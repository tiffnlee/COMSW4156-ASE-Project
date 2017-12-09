# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='rank',
            field=models.IntegerField(default=0, verbose_name='rank'),
        ),
        migrations.AlterField(
            model_name='search',
            name='region_choices',
            field=models.CharField(choices=[('NA', 'North America'), ('EU', 'Europe'), ('AS', 'Asia'), ('OC', 'Oceania'), ('SA', 'South America'), ('SEA', 'South East Asia'), ('KR/JP', 'Korea/Japan')], max_length=5, verbose_name='region preference'),
        ),
    ]