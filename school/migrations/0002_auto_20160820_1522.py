# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-20 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolprofiles',
            old_name='name',
            new_name='schname',
        ),
    ]