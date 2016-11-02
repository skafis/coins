# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-17 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplineCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blacklist', models.CharField(max_length=10000, verbose_name='Blacklist name')),
                ('blacklistdate', models.DateField(verbose_name='Entry date')),
                ('whitelist', models.CharField(max_length=10000, verbose_name='Exam name')),
                ('whitelistdate', models.DateField(verbose_name='Whitelist date')),
            ],
            options={
                'verbose_name_plural': 'Discipline Case',
            },
        ),
    ]
