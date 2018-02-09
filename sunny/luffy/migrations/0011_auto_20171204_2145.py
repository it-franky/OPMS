# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luffy', '0010_remove_todolist_exec_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['important'], 'verbose_name': 'TodoList', 'verbose_name_plural': 'TodoList'},
        ),
        migrations.AddField(
            model_name='todolist',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
