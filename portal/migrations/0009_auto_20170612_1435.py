# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-12 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20170601_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='cat_products', to='portal.Category'),
        ),
    ]
