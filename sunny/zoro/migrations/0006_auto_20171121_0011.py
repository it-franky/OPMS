# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoro', '0005_fitnessrecords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessrecords',
            name='content',
            field=models.TextField(max_length=100),
        ),
    ]
