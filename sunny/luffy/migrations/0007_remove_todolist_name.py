# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luffy', '0006_auto_20171115_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='name',
        ),
    ]
