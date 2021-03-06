# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-04 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pos_portal', '0014_merchants_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentaccountswallets',
            name='is_locked',
            field=models.BooleanField(default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentaccountswallets',
            name='studentprofiles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.StudentProfiles', verbose_name='Bank Acc'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='ref_no',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='trace_no',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
