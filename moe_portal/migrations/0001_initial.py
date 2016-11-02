# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-20 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bursery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=19, verbose_name='Amount (KSH)')),
                ('county', models.CharField(max_length=5000, verbose_name='County')),
                ('sch_bank_acc', models.CharField(max_length=5000, verbose_name='School BANK Acc')),
                ('financial_year', models.CharField(default=1, max_length=5000, verbose_name='Financial year')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bursery_name', to='school.SchoolProfiles', verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Bursery',
            },
        ),
        migrations.CreateModel(
            name='TutionFunds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=5000, verbose_name='County')),
                ('bankname', models.CharField(default=1, max_length=5000, verbose_name='County')),
                ('sch_bank_acc', models.CharField(max_length=5000, verbose_name='School BANK Acc')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=19, verbose_name='Amount (KSH)')),
                ('transactiontype', models.CharField(max_length=5000, verbose_name='transaction type')),
                ('transactiondate', models.DateField(default=django.utils.timezone.now, max_length=5000, verbose_name='Date')),
                ('financial_year', models.CharField(default=1, max_length=5000, verbose_name='Financial year')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutionfunds_name', to='school.SchoolProfiles', verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Tution Funds',
            },
        ),
    ]