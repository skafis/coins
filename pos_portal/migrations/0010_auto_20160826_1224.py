# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-26 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20160826_1224'),
        ('pos_portal', '0009_auto_20160826_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentaccounts',
            name='studentprofiles',
        ),
        migrations.RemoveField(
            model_name='studentaccountswallets',
            name='bank_acc',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='studentaccounts',
        ),
        migrations.AddField(
            model_name='studentaccountswallets',
            name='studentprofiles',
            field=models.ForeignKey(default=1234, on_delete=django.db.models.deletion.CASCADE, to='students.StudentProfiles', verbose_name='Bank Acc'),
        ),
        migrations.DeleteModel(
            name='StudentAccounts',
        ),
    ]
