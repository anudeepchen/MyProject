# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_posting', '0002_auto_20150809_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_details',
            name='role',
            field=models.CharField(max_length=120, default=''),
        ),
    ]
