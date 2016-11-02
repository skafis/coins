# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-20 11:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=5000)),
                ('secondname', models.CharField(max_length=5000)),
                ('lastname', models.CharField(max_length=5000)),
                ('phonenumber', models.CharField(max_length=5000)),
                ('email', models.CharField(max_length=5000)),
                ('posnumber', models.CharField(max_length=5000)),
            ],
            options={
                'verbose_name_plural': 'Merchants',
            },
        ),
        migrations.CreateModel(
            name='Pos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('posnumber', models.CharField(max_length=5000)),
                ('accountnumber', models.CharField(max_length=5000)),
                ('serialnum', models.CharField(max_length=5000)),
            ],
            options={
                'verbose_name_plural': 'Pos',
            },
        ),
        migrations.AddField(
            model_name='merchants',
            name='pos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pos_portal.Pos'),
        ),
        migrations.AddField(
            model_name='merchants',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
    ]
