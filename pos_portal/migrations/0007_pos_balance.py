# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-26 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_portal', '0006_auto_20160826_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='pos',
            name='balance',
            field=models.CharField(default=100, max_length=5000),
        ),
    ]