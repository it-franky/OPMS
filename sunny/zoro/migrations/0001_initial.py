# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cycling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riding_date', models.DateField()),
                ('distance', models.FloatField()),
                ('duration', models.TimeField()),
                ('route', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=50)),
                ('load', models.FloatField(default=0)),
                ('count', models.IntegerField(default=12)),
                ('groups', models.IntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
