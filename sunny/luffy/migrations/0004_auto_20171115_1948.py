# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luffy', '0003_auto_20171115_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luffy.Members'),
        ),
    ]
