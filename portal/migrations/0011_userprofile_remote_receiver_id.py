# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-12 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_userprofile_remote_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='remote_receiver_id',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
