# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoro', '0004_auto_20171115_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exec_date', models.DateField()),
                ('content', models.CharField(max_length=100)),
                ('place', models.CharField(choices=[('gym', '健身房'), ('home', '在家')], default='gym', max_length=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='courses/%Y/%m')),
            ],
            options={
                'verbose_name': '健身记录',
                'verbose_name_plural': '健身记录',
            },
        ),
    ]
