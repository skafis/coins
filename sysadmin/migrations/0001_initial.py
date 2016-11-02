# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-20 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorytype', models.CharField(max_length=255, verbose_name='Category Type')),
            ],
            options={
                'verbose_name_plural': 'Category Type',
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(max_length=255, verbose_name='Classes')),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Country',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countyname', models.CharField(max_length=255, verbose_name='County')),
            ],
            options={
                'verbose_name_plural': 'County',
            },
        ),
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dormitory', models.CharField(max_length=255, verbose_name='Dormitory')),
            ],
            options={
                'verbose_name_plural': 'Dormitories',
            },
        ),
        migrations.CreateModel(
            name='EntryYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryyear', models.CharField(max_length=255, verbose_name='EntryYear')),
                ('currentyear', models.BooleanField(verbose_name='Current Year')),
            ],
            options={
                'verbose_name_plural': 'Entry Year',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=255, verbose_name='Gender')),
                ('entryyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year')),
            ],
            options={
                'verbose_name_plural': 'Gender',
            },
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.CharField(max_length=255, verbose_name='Grades')),
                ('points', models.IntegerField(default=0, verbose_name='Points')),
            ],
            options={
                'verbose_name_plural': 'Grades',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=255, verbose_name='House')),
                ('entryyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year')),
            ],
            options={
                'verbose_name_plural': 'House',
            },
        ),
        migrations.CreateModel(
            name='Months',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=255, verbose_name='Months')),
                ('entryyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year')),
            ],
            options={
                'verbose_name_plural': 'Months',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper', models.CharField(max_length=255, verbose_name='Papers')),
                ('paper_code', models.CharField(max_length=255, unique=True, verbose_name='Paper Code')),
                ('entryyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year')),
            ],
            options={
                'verbose_name_plural': 'Papers',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentmethods', models.CharField(max_length=255, verbose_name='Payment Method')),
            ],
            options={
                'verbose_name_plural': 'Payment Methods',
            },
        ),
        migrations.CreateModel(
            name='SchoolType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schooltype', models.CharField(max_length=255, verbose_name='School Type')),
            ],
            options={
                'verbose_name_plural': 'School Types',
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=255, verbose_name='Stream')),
                ('entryyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year')),
            ],
            options={
                'verbose_name_plural': 'stream',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('subject_code', models.CharField(max_length=255, unique=True, verbose_name='Subject Code')),
                ('entryyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year')),
            ],
            options={
                'verbose_name_plural': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='SystemConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command_label', models.CharField(max_length=255, unique=True, verbose_name='Command Label')),
                ('command', models.CharField(max_length=255, verbose_name='command')),
            ],
            options={
                'verbose_name_plural': 'System Config',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=255, verbose_name='Term')),
                ('entryyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year')),
            ],
            options={
                'verbose_name_plural': 'Term',
            },
        ),
        migrations.CreateModel(
            name='VoteHeads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voteheads', models.CharField(max_length=255, verbose_name='Vote heads')),
                ('entryyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year')),
            ],
            options={
                'verbose_name_plural': 'Vote heads',
            },
        ),
        migrations.AddField(
            model_name='dormitory',
            name='entryyear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year'),
        ),
        migrations.AddField(
            model_name='classes',
            name='entryyear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year'),
        ),
        migrations.AddField(
            model_name='categorytype',
            name='entryyear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year'),
        ),
        migrations.AddField(
            model_name='category',
            name='entryyear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysadmin.EntryYear', verbose_name='Entry year'),
        ),
    ]
