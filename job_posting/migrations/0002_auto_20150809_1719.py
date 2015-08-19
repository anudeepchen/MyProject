# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_posting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_details',
            name='job_type',
            field=models.CharField(max_length=2, choices=[('FT', 'Full-time'), ('CO', 'Contractor'), ('IN', 'Intern')], default=''),
        ),
    ]
