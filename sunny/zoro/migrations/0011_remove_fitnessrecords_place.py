# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-01 21:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoro', '0010_auto_20171202_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitnessrecords',
            name='place',
        ),
    ]