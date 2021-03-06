# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-24 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sysadmin', '0001_initial'),
        ('school', '0004_auto_20160820_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entryyear_entryyear', to='sysadmin.EntryYear', verbose_name='EntryYear')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.SchoolProfiles', verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'EntryYear',
            },
        ),
        migrations.AlterUniqueTogether(
            name='entryyear',
            unique_together=set([('name', 'entryyear')]),
        ),
    ]
