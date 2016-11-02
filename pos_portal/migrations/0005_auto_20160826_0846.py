# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-26 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos_portal', '0004_auto_20160826_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchants',
            name='pos',
        ),
        migrations.RemoveField(
            model_name='pos',
            name='name',
        ),
        migrations.AddField(
            model_name='pos',
            name='merchants',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pos_portal.Merchants'),
        ),
    ]