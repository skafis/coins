# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-25 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20160902_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dormitory',
            name='dormitory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_dormitory', to='sysadmin.Dormitory', verbose_name='Dormitory'),
        ),
    ]
