# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luffy', '0003_auto_20170918_2259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='exec_address',
            new_name='exec_place',
        ),
    ]
