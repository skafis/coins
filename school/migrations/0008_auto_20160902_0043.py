# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-02 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20160902_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofiles',
            name='balance',
            field=models.CharField(default='1', max_length=5000),
        ),
        migrations.AddField(
            model_name='schoolprofiles',
            name='noofmerchants',
            field=models.CharField(default='1', max_length=5000),
        ),
    ]
