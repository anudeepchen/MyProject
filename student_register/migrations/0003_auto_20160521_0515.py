# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0002_auto_20150809_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_profile',
            name='phone',
        ),
        migrations.AddField(
            model_name='student_profile',
            name='location',
            field=models.CharField(default=b'', max_length=120),
        ),
    ]
