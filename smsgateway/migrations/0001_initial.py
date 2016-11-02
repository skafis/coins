# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-20 11:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=5000, verbose_name='country')),
                ('phoneno', models.CharField(max_length=255, verbose_name='Phone-no')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Group')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.SchoolProfiles', verbose_name='Name')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name_plural': 'Phone Book',
            },
        ),
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('deliverystatus', models.CharField(max_length=255, verbose_name='Delivery status')),
                ('messageid', models.CharField(max_length=255, verbose_name='Transaction id')),
                ('cost', models.CharField(max_length=255, verbose_name='Cost')),
                ('sendtime', models.DateTimeField(verbose_name='Send time')),
                ('deleverytime', models.DateTimeField(max_length=255, verbose_name='Delivery time')),
                ('latency', models.IntegerField(default=0, verbose_name='Latency in Seconds')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsgateway.PhoneBook', verbose_name='Phone Book')),
            ],
            options={
                'verbose_name_plural': 'Sms',
            },
        ),
    ]
