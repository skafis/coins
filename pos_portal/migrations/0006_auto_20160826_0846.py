# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-26 08:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos_portal', '0005_auto_20160826_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pos',
            old_name='merchants',
            new_name='merchant',
        ),
    ]
